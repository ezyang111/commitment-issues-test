# openai_integration/prompt_builder.py

class PromptBuilder:
    def __init__(self, template='simple'):
        self.template = template

    def construct_prompt(self, changes, feedback=None, old_message=None):
        base_prompt = (
            "You are an AI assistant tasked with generating commit messages based strictly on the provided git diff changes. "
            "Please adhere to the following instructions carefully and do not deviate from the format or include any additional information.\n\n"
            "**Format:**\n"
            "<ChangeType> | <ImpactArea>: <TLDR>\n\n"
            "**Instructions:**\n"
            "- **ChangeType**: Select **only one** from [feature, bugfix, refactor, docs, test, chore].\n"
            "- **ImpactArea**: Specify the affected part of the project (e.g., 'frontend', 'backend', 'database', 'user interface').\n"
            "- **TLDR**: Write a concise, one-line summary of the changes in imperative mood (e.g., 'Fix crash when user inputs empty string').\n"
            "- Do not include any details beyond the TLDR unless instructed.\n"
            "- **Do not** add any sections or information not specified in the format.\n"
        )
        if self.template == 'complex':
            base_prompt += (
                "\nAfter the TLDR, provide a detailed description of the changes starting on a new line. "
                "The detailed description should explain what was changed and why, using clear and concise language."
            )

        # Examples
        base_prompt += (
            "\n\n**Examples:**\n"
            "feature | backend: Add user authentication module\n"
            "bugfix | frontend: Fix alignment issue on login page\n"
            "refactor | database: Optimize query performance\n"
        )

        user_message = f"\n**Git Diff Changes:**\n```\n{changes}\n```\n"

        if feedback and old_message:
            user_message += (
                f"\n**Previous Commit Message:**\n{old_message}\n"
                f"\n**User Feedback:**\n{feedback}\n"
                "Please revise the commit message accordingly, strictly following the format and instructions."
            )

        return f"{base_prompt}{user_message}"

