# Commitment Issues 

A Command Line Interface (CLI) tool that generates and manages Git commit messages.

## Installation

### Prerequisites

- **Python 3.7+**
- **Git**

### Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/edwardyeung04/commitment-issues.git
    cd commitment-issues
    ```

2. **Install Dependencies:**

    **Important:** This program requires OpenAI package version `0.28`.

    ```bash
    pip install openai==0.28 python-dotenv
    ```

    Alternatively, using `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

    **`requirements.txt` Content:**

    ```
    openai==0.28
    python-dotenv
    ```

## Setup

1. **Create a `.env` File:**

    In the project root, create a file named `.env`:

    ```bash
    touch .env
    ```

2. **Add Your OpenAI API Key:**

    Open `.env` and add:

    ```
    OPENAI_API_KEY=your_openai_api_key_here
    ```

    **Replace `your_openai_api_key_here` with your actual OpenAI API key.**

    **Note:** The `.gitignore` includes `.env` to keep your API key private.

## Usage

### Regular Workflow

1. **Make Code Changes:**

    Develop your code as usual.

2. **Stage Changes:**

    ```bash
    git add .
    ```

3. **Generate and Commit Message:**

    - **Using Default Template (Simple):**

        Simply run the `commit` command without specifying the template. This uses the default `simple` template.

        ```bash
        python cli.py commit
        ```

        **What Happens:**
        - Generates a commit message using the `simple` template (token limit: 500).
        - Automatically runs `git commit -m "generated message"`.
        - Displays the commit message in the terminal for your reference.

    - **Specifying Template Complexity:**

        Choose between `simple` and `complex` templates by using the `-m` or `--template` flag **after** the `commit` subcommand.

        ```bash
        python cli.py commit -m c
        ```

        **Options:**
        - `-m`, `--template`: Select the commit message template complexity.
            - `c`: Provides a **complex** commit message.
            - `s`: Provides a **simple** commit message. *(Default)*

        **Example:**

        ```bash
        python cli.py commit -m s
        ```

4. **Push Changes:**

    After committing, push your changes to the remote repository as usual.

    ```bash
    git push
    ```

### Additional Commands

- **Filter Commit History:**

    ```bash
    python cli.py filter -c bugfix -i backend
    ```

    **Options:**
    - `-c`, `--change-type`: Filter commits by change type (e.g., feature, bugfix).
    - `-i`, `--impact-type`: Filter commits by impact area (e.g., frontend, backend).

- **View Help:**

    To see all available commands and options, use the `--help` flag.

    ```bash
    python cli.py --help
    ```

    **Example Output:**

    ```
    usage: cli.py [-h] {commit,filter} ...

    CLI tool to generate and manage commit messages.

    positional arguments:
      {commit,filter}       Commands
        commit              Generate and commit a message.
        filter              Filter commit history.

    options:
      -h, --help            show this help message and exit
    ```

## Notes

- **Environment Security:** Ensure `.env` is not committed to your repository to protect your API keys.
- **OpenAI Version:** Use `openai==0.28` as newer versions may lack required features.
- **Argument Placement:** Flags are now subcommand-specific and should be placed **after** the respective subcommand.
