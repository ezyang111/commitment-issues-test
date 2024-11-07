# cli.py

"""
This script provides a command-line interface for generating commit messages 
and filtering git commit history.

Functions:
- load_environment(): Loads environment variables.
- main(): Handles user interactions for generating commit messages or filtering
 commits based on the provided command.
"""

import os
import sys
import subprocess
from dotenv import load_dotenv
from cli_interface.user_interface import UserInterface
from cli_interface.message_maker import MessageMaker
from git_scripts.git_diff_fetcher import GitDiffFetcher
from git_scripts.git_history_analyzer import GitHistoryAnalyzer
from rich import print

def load_environment():
    """Load environment variables from .env file."""
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        sys.exit(1)

def main(): # pylint: disable=too-many-branches
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
                    subprocess.run(["git", "commit", "-m", commit_message], check=True)
                    print(f"Changes committed with message: {commit_message}")
                except subprocess.CalledProcessError as e:
                    ui.show_error(f"Error committing changes: {e}")
                break
            if user_input == 'r':
                # Regenerate the commit message
                feedback = ui.prompt_feedback()
                commit_message = message_maker.regenerate_message(changes, feedback) # pylint: disable=no-member
            elif user_input == 'e':
                commit_message = ui.prompt_manual_edit(commit_message)
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
            ui.display_commits_paginated(filtered_commits)
        else:
            print("[bold red]No commits found matching the criteria.[/bold red]")
    else:
        # If no command is provided, show help
        ui.parser.print_help()

if __name__ == "__main__":
    main()
