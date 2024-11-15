# Commitment Issues

Commitment Issues is a Command Line Interface (CLI) tool designed to simplify and enhance the creation of Git commit messages. It offers developers the ability to generate messages using customizable templates, accommodating both straightforward and detailed message styles. With features for regenerating and editing commit messages, Commitment Issues provides flexibility for refining messages as needed. This tool helps ensure that commit messages are consistent and informative, improving code communication and saving valuable development time.

## Why Use Commitment Issues?

Commitment Issues takes the hassle out of writing commit messages, making them clear, informative, and meaningful—without all the extra effort. Developers often overlook the impact of a well-written commit message, leading to vague or even cryptic notes that don't communicate the true value of code changes. Commitment Issues solves this by simplifying the process: just run a single command, and voilà, you're done! Plus, if you prefer a personalized touch, you can easily customize generated messages to fit your style, saving you from starting from scratch and only having to write minor tweaks. Make your commits better with Commitment Issues; your team will thank you!

## Installation

*In development*

    pip install cissue

### Prerequisites

- **Python 3.7+**
- **Git**

### Installation Instructions

1. **Clone the Repository:**

        git clone https://github.com/edwardyeung04/commitment-issues.git
        cd commitment-issues

2. **Install Dependencies:**

    **Important:** This program requires OpenAI package version `0.28`.

        pip install openai==0.28 python-dotenv

    Alternatively, using `requirements.txt`:

        pip install -r requirements.txt

    **`requirements.txt` Content:**

        openai==0.28
        python-dotenv
        pytest
        pylint

## Setup

1. **Create a `.env` File:**

    In the project root, create a file named `.env`:

        touch .env

2. **Add Your OpenAI API Key:**

    Open `.env` and add:

        OPENAI_API_KEY=your_openai_api_key_here

    **Replace `your_openai_api_key_here` with your actual OpenAI API key.**

    **Note:** The `.gitignore` includes `.env` to keep your API key private.

## Usage

### Regular Workflow

1. **Make Code Changes:**

    Develop your code as usual.

2. **Stage Changes:**

        git add .

3. **Generate and Commit Message:**

    - **Using Default Template (Simple):**

        Simply run the `commit` command without specifying the template. This uses the default `simple` template.

            python cli.py commit

        **What Happens:**

        - Generates a commit message using the `simple` template (token limit: 500).
        - Displays the generated commit message.
        - Prompts for action: accept, regenerate, edit, or quit.

    - **Specifying Template Complexity:**

        Choose between `simple` and `complex` templates by using the `-m` or `--template` flag **after** the `commit` subcommand.

            python cli.py commit -m c

        **Options:**

        - `-m`, `--template`: Select the commit message template complexity.
            - `c`: Provides a **complex** commit message.
            - `s`: Provides a **simple** commit message. *(Default)*

        **Example:**

            python cli.py commit -m s

4. **Check Message:**

    After generating the commit message, you will see four options:

        Generated commit message:
        <changetype> | <impact area>: message

        Do you want to (a)ccept this message, (r)egenerate, (e)dit, or (q)uit?

    - **Accept (a):** Automatically commits the changes with the generated message.
    - **Regenerate (r):** Generates a new message and shows suggestions.
    - **Edit (e):** Opens an editor to write your own message.
    - **Quit (q):** Exits without committing.

5. **Push Changes:**

    After committing, push your changes to the remote repository as usual.

        git push

### Additional Commands

- **Filter Commit History:**

        python cli.py filter -c bugfix -i backend

    **Options:**

    - `-c`, `--change-type`: Filter commits by change type (e.g., feature, bugfix).
    - `-i`, `--impact-type`: Filter commits by impact area (e.g., frontend, backend).

- **Reformat Commit History *(Work in Progress)*:**

    The **Reformat Commit History** feature allows you to update previous commit messages to align with Commitment Issues' current structured format. This feature is currently under development and aims to help maintain a consistent and informative commit history.

    #### Features

    - **Reformat by Commit ID:** Update a specific commit message using its commit ID.

        ```bash
        python cli.py reformat --commit-id <commit_id>
        ```

    - **Reformat by Number of Commits:** Update the last **N** commit messages.

        ```bash
        python cli.py reformat --last <number>
        ```

    - **Reformat by Time Period:** Update commits within a specific time frame.

        ```bash
        python cli.py reformat --period "YYYY-MM-DD:YYYY-MM-DD"
        ```

    #### Options

    - `--commit-id <commit_id>`: Reformat a specific commit by its ID.
    - `--last <number>`: Reformat the last **N** commits.
    - `--period "YYYY-MM-DD:YYYY-MM-DD"`: Reformat commits within a specific date range.

    #### Usage Examples

    - **Reformat a Specific Commit:**

        To reformat a commit with the ID `abc1234`:

        ```bash
        python cli.py reformat --commit-id abc1234
        ```

    - **Reformat the Last 10 Commits:**

        To reformat the most recent 10 commit messages:

        ```bash
        python cli.py reformat --last 10
        ```

    - **Reformat Commits Within a Date Range:**

        To reformat commits made between January 1, 2024, and June 30, 2024:

        ```bash
        python cli.py reformat --period "2024-01-01:2024-06-30"
        ```

    #### Important Notes

    - **Backup Your Repository:** Rewriting commit history can have significant effects, especially for shared or public repositories. Ensure you have backups before performing any reformatting operations.

    - **Collaborator Coordination:** If you're working in a team, inform all collaborators before rewriting history to avoid discrepancies in their local repositories.

    - **Immutable History:** Altering commit history changes commit hashes, which may lead to discrepancies if not managed carefully.

- **View Help:**

    To see all available commands and options, use the `--help` flag.

        python cli.py --help

    **Example Output:**

        usage: cli.py [-h] {commit,filter,reformat} ...

        CLI tool to generate and manage commit messages.

        positional arguments:
          {commit,filter,reformat}
                                Commands
              commit              Generate and commit a message.
              filter              Filter commit history.
              reformat            Reformat commit history.

        options:
          -h, --help            show this help message and exit

## Reporting a Bug

Users are welcome to submit a Git Issue when encountering a new bug that is not already listed as a Known Bug (more info below). We require that the content of the Git Issue adhere to the information requested in the template located in `.github/ISSUE_TEMPLATE/bug-report-template.md`. When creating a new Git Issue, there is an option to import the template directly into the text box for ease of use. The user should assign the label `bug` to further indicate this Git Issue as bug-related.

As soon as this Git Issue is submitted, it will be assigned the `unresolved` and `pending review` labels by default to communicate that it is an open bug that is pending verification from the development team. Once the issue has been verified as a valid bug (by reviewing the contents of the Git Issue), a member of the team will remove the `pending review` label and clarify its unresolved status by tagging it `unresolved`. The next step for developers is to tag the open issue with `in progress` to indicate that they have claimed responsibility to resolve that bug. Once a developer resolves the bug, the `in progress` and `unresolved` labels will be replaced with `resolved` to indicate that the bug has been fixed.

### Known Bugs

A list of Known Bugs can be found by filtering the Git Issues by the `bug` label. More specifically, the `in progress` label can be added as a filter to show all bugs that are still unresolved and in progress of being fixed. A list of resolved bugs can be found by filtering by `bug` and `resolved`.

## Notes

- **Environment Security:** Ensure `.env` is not committed to your repository to protect your API keys.
- **OpenAI Version:** Use `openai==0.28` as newer versions may lack required features.
- **Argument Placement:** Flags are now subcommand-specific and should be placed **after** the respective subcommand.
- **Manual Git Commands:** Users are still responsible to manually `add` and `push` their code changes via Git. Commitment Issues only assists in the middle step of committing the changes.

---

By introducing the Reformat Commit History feature, Commitment Issues aims to help you maintain a clean and consistent commit history, enhancing the clarity and professionalism of your project's version control. Stay tuned for updates as we continue to enhance this functionality!
