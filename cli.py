import openai
import subprocess
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

MAX_MESSAGE_TOKENS = 400

def get_git_diff():
    """
    Get the changes from the git diff command that are staged for commit.
    """
    try:
        # Check if there are any staged changes
        staged_check = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True, check=True)
        if not staged_check.stdout.strip():
            print("No staged changes found. Have you added your changes with 'git add'?")
            return None

        # Get the diff for staged changes
        result = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True, check=True)
        if not result.stdout.strip():
            print("Git diff command succeeded, but returned empty output.")
            return None
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running git command: {e}")
        print(f"Command output: {e.output}")
        print(f"Command stderr: {e.stderr}")
        return None
    except Exception as e:
        print(f"Unexpected error in get_git_diff: {e}")
        return None

def generate_commit_message(changes):
    """
    Generate a commit message using OpenAI's GPT model based on git diff changes.
    """
    messages = [
        {"role": "system", "content": "You are an AI assistant that generates commit messages based on git diff changes. Format the commit message as follows:\n<ChangeType> | <ImpactArea>: <TLDR>\n\nWhere:\n- ChangeType is one of: feature, bugfix, refactor, docs, test, chore\n- ImpactArea is the part of the project affected (e.g., frontend, backend, database)\n- TLDR is a brief, one-line summary of the changes"},
        {"role": "user", "content": f"Generate a commit message for the following changes:\n{changes}"}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=MAX_MESSAGE_TOKENS,
        )

        commit_message = response.choices[0].message["content"].strip()
        return commit_message
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None

def commit_changes(commit_message):
    """
    Run the git commit command with the generated commit message.
    """
    try:
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print(f"Changes committed with message: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"Error committing changes: {e}")

def main():
    changes = get_git_diff()
    if not changes:
        print("No changes detected.")
        return

    print("Generating commit message...")
    commit_message = generate_commit_message(changes)

    if not commit_message:
        print("Failed to generate commit message.")
        return

    print(f"Generated commit message:\n{commit_message}")

    # Commit the changes using the generated commit message
    commit_changes(commit_message)

if __name__ == "__main__":
    main()
