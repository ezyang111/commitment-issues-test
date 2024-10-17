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
        result = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running git diff: {e}")
        return None

def generate_commit_message(changes):
    """
    Generate a commit message using OpenAI's GPT model based on git diff changes.
    """
    messages = [
        {"role": "user", "content": f"Summarize the following changes:\n{changes}"}
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
