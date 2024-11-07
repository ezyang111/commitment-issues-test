# cli_interface/user_interface.py

import argparse
import os
import subprocess
import sys
import tempfile
from rich import print
from rich.table import Table
import click

class UserInterface:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="CLI tool to generate and manage commit messages."
        )
        self._setup_arguments()

    def _setup_arguments(self):
        subparsers = self.parser.add_subparsers(dest='command', help='Commands')

        # Commit command
        commit_parser = subparsers.add_parser('commit', help='Generate and commit a message.')
        commit_parser.add_argument(
            '-m', '--template',
            choices=['c', 's'],  # 'c' for complex, 's' for simple
            default='s',
            help='Select the commit message template complexity.' +
                 '(c: complex, s: simple) (Default: s)'
        )

        # Filter command
        filter_parser = subparsers.add_parser('filter', help='Filter commit history.')
        filter_parser.add_argument(
            '-c', '--change-type',
            type=str,
            help='Filter by change type (e.g., feature, bugfix).'
        )
        filter_parser.add_argument(
            '-i', '--impact-type',
            type=str,
            help='Filter by impact area (e.g., frontend, backend).'
        )

        # Help flag is automatically handled by argparse

    def parse_args(self):
        return self.parser.parse_args()

    def display_commit_message(self, commit_message):
        print(f"\nGenerated commit message:\n{commit_message}")

    def prompt_user_action(self):
        return input("\nDo you want to (a)ccept this message," +
                     " (r)egenerate, (e)dit, or (q)uit? ").lower()

    def prompt_feedback(self):
        return input("Please provide feedback for regeneration (or press Enter to skip): ")

    def prompt_manual_edit(self, initial_message):
        with tempfile.NamedTemporaryFile(suffix=".tmp") as temp_file:
            # Write initial commit message
            temp_file.write(initial_message.encode())
            temp_file.flush()

            # Open temp_file using user's editor
            editor = os.getenv("EDITOR", "vim")
            subprocess.run([editor, temp_file.name])

            # Read edited commit message
            temp_file.seek(0)
            edited_message = temp_file.read().decode()

        return edited_message

    def show_error(self, message):
        print(f"Error: {message}", file=sys.stderr)

    def display_commits_paginated(self, commits, page_size=5):
        table = Table(title="Filtered Commits")
        table.add_column("Hash", style="cyan", no_wrap=True)
        table.add_column("Subject", style="magenta")
        table.add_column("Author", style="green")
        table.add_column("Date", style="yellow")

        total_commits = len(commits)
        current_index = 0

        while current_index < total_commits:
            # Add rows for the next set of commits
            for i in range(current_index, min(current_index + page_size, total_commits)):
                commit = commits[i]
                table.add_row(
                    commit['hash'],
                    commit['subject'],
                    commit['author'],
                    commit['date']
                )

            # Print the updated table
            print(table)

            current_index += page_size

            # Check if there are more commits to show
            if current_index < total_commits:
                click.confirm("Press Enter to show more commits", default=True, abort=True)
            else:
                print("[bold green]End of commits list.[/bold green]")
