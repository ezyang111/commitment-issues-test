# cli.py

import os
from dotenv import load_dotenv
from cli_interface.user_interface import UserInterface
from cli_interface.message_maker import MessageMaker
from git_scripts.git_diff_fetcher import GitDiffFetcher
from git_scripts.git_history_analyzer import GitHistoryAnalyzer

def load_environment():
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        exit(1)

def main():
    load_environment()

    ui = UserInterface()
    args = ui.parse_args()

    git_fetcher = GitDiffFetcher()
    git_analyzer = GitHistoryAnalyzer()

    if args.command == 'commit':
        changes = git_fetcher.get_staged_diff()
        if not changes:
            print("No changes detected.")
            return

        # Map 'c' to 'complex' and 's' to 'simple'
        template_map = {'c': 'complex', 's': 'simple'}
        selected_template = template_map.get(args.template, 'simple')

        message_maker = MessageMaker(template=selected_template)

        commit_message = message_maker.generate_message(changes)

        while True:
            if not commit_message:
                ui.show_error("Failed to generate commit message.")
                return

            ui.display_commit_message(commit_message)

            user_input = ui.prompt_user_action()

            if user_input == 'a':
                # Commit the changes using the generated commit message
                try:
                    import subprocess
                    subprocess.run(["git", "commit", "-m", commit_message], check=True)
                    print(f"Changes committed with message: {commit_message}")
                except subprocess.CalledProcessError as e:
                    ui.show_error(f"Error committing changes: {e}")
                break
            elif user_input == 'r':
                feedback = ui.prompt_feedback()
                commit_message = message_maker.regenerate_message(changes, feedback, change_type, impact_area)
            elif user_input == 'q':
                print("Quitting without committing changes.")
                break
            else:
                ui.show_error("Invalid input. Please try again.")
    elif args.command == 'filter':
        filtered_commits = git_analyzer.filter_commits(
            change_type=args.change_type,
            impact_area=args.impact_type
        )
        if filtered_commits:
            for commit in filtered_commits:
                print(f"{commit['hash']} - {commit['subject']} by {commit['author']} on {commit['date']}")
        else:
            print("No commits found matching the criteria.")
    else:
        # If no command is provided, show help
        ui.parser.print_help()

if __name__ == "__main__":
    main()
