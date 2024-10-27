# openai_integration/response_processor.py

import re

class ResponseProcessor:
    def __init__(self):
        pass

    def process_response(self, raw_response):
        if not raw_response:
            return None

        # Validate the structure using regex
        pattern = r"^(?P<ChangeType>feature|bugfix|refactor|docs|test|chore) \| (?P<ImpactArea>\w+): (?P<TLDR>.+)$"
        match = re.match(pattern, raw_response, re.DOTALL)

        if not match:
            print("Generated commit message does not match the required format.")
            return None

        # Further processing can be done here if needed
        return raw_response
