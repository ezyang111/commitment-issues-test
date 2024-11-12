# openai_integration/response_processor.py

import re

class ResponseProcessor:
    def __init__(self):
        pass

    def process_response(self, raw_response):
        if not raw_response:
            return None

        response_text = raw_response.strip()

        # Define a regex pattern to match the exact commit message format
        pattern = (
            r"^(?P<ChangeType>feature|bugfix|refactor|docs|test|chore)"
            r"\s*\|\s*(?P<ImpactArea>[\w\s]+):\s*(?P<TLDR>.+?)(?:\n|$)"
        )

        match = re.match(pattern, response_text, re.IGNORECASE)

        if not match:
            print("Generated commit message does not match the required format.")
            print("Response from GPT:\n", response_text)
            return None

        change_type = match.group('ChangeType').strip().lower()
        impact_area = match.group('ImpactArea').strip()
        tldr = match.group('TLDR').strip()

        # Build the commit message
        commit_message = f"{change_type} | {impact_area}: {tldr}"

        # Check for detailed description if template is complex
        detailed_description = ''
        if '\n\n' in response_text:
            detailed_description = response_text.split('\n\n', 1)[1].strip()
            commit_message += f"\n\n{detailed_description}"

        return commit_message
