# openai_integration/response_processor.py

import re

class ResponseProcessor:
    SIMPLE_PATTERN = re.compile(
        r"^(feat|feature|bugfix|fix|refactor|docs|doc|test|tests|chore)\s*\|\s*([\w\s\-]+):\s*(.+)$",
        re.IGNORECASE
    )
    COMPLEX_SUMMARY_PATTERN = SIMPLE_PATTERN
    # Detailed description can be any non-empty text

    def __init__(self, template='simple'):
        self.template = template.lower()

    def process_response(self, raw_response):
        if not raw_response:
            print("No response received from GPT.")
            return None

        # Remove any leading/trailing whitespace
        response_text = raw_response.strip()

        if self.template == 'complex':
            # Expecting two parts: summary and detailed description
            parts = response_text.split('\n\n', 1)
            if len(parts) != 2:
                print("Generated commit message is missing the detailed description.")
                print("Response from GPT:\n", response_text)
                return None

            summary, description = parts
            summary = summary.strip()
            description = description.strip()

            # Validate the summary
            if not self.validate_summary(summary):
                print("Generated commit summary does not match the expected format.")
                print(f"Summary: {summary}")
                return None

            # Ensure detailed description is not empty
            if not description:
                print("Detailed description is empty.")
                print("Response from GPT:\n", response_text)
                return None

            # Normalize ChangeType
            summary = self.normalize_change_type(summary)

            # Build the commit message
            commit_message = f"{summary}\n\n{description}"
            return commit_message

        else:  # 'simple'
            # Expecting only the summary
            summary = response_text
            if not self.validate_summary(summary):
                print("Generated commit message does not match the required format.")
                print("Response from GPT:\n", response_text)
                return None

            # Normalize ChangeType
            summary = self.normalize_change_type(summary)

            return summary

    def validate_summary(self, message):
        return bool(self.SIMPLE_PATTERN.match(message))

    def normalize_change_type(self, message):
        match = self.SIMPLE_PATTERN.match(message)
        if not match:
            return message  # Already validated, should not happen

        change_type = match.group(1).lower()
        impact_area = match.group(2).strip().lower()
        tldr = match.group(3).strip()

        # Normalize ChangeType
        change_type_mapping = {
            'feat': 'feature',
            'fix': 'bugfix',
            'doc': 'docs',
            'tests': 'test',
        }
        change_type = change_type_mapping.get(change_type, change_type)

        normalized_message = f"{change_type} | {impact_area}: {tldr}"
        return normalized_message
