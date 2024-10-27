# openai_integration/prompt_builder.py

import os
import json

class PromptBuilder:
    def __init__(self, template='simple'):
        self.template = template

    def construct_prompt(self, changes, change_type, impact_area, feedback=None):
        base_prompt = (
            "You are an AI assistant that generates commit messages based on git diff changes. "
            "Format the commit message as follows:\n"
            "<ChangeType> | <ImpactArea>: <TLDR>\n\n"
            "Where:\n"
            "- ChangeType is one of: feature, bugfix, refactor, docs, test, chore\n"
            "- ImpactArea is the part of the project affected (e.g., frontend, backend, database)\n"
            "- TLDR is a brief, one-line summary of the changes"
        )
        if self.template == 'complex':
            base_prompt += (
                "\n\nProvide a detailed description following the TLDR."
            )

        user_message = f"Generate a commit message for the following changes:\n{changes}\n"
        user_message += f"ChangeType: {change_type}\nImpactArea: {impact_area}\n"

        if feedback:
            user_message += f"Feedback: {feedback}\n"

        return f"{base_prompt}\n\n{user_message}"
