# cli_interface/message_maker.py

from openai_integration.prompt_builder import PromptBuilder
from openai_integration.gpt_client import GPTClient
from openai_integration.response_processor import ResponseProcessor

class MessageMaker:
    def __init__(self, template='simple'):
        self.prompt_builder = PromptBuilder(template)
        self.gpt_client = GPTClient()
        self.response_processor = ResponseProcessor()

    def generate_message(self, changes, feedback=None, old_message=None):
        prompt = self.prompt_builder.construct_prompt(changes, feedback, old_message)
        raw_response = self.gpt_client.send_prompt(prompt)
        commit_message = self.response_processor.process_response(raw_response)
        return commit_message