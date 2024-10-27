# cli_interface/message_maker.py

import re
import json
from openai_integration.prompt_builder import PromptBuilder
from openai_integration.gpt_client import GPTClient
from openai_integration.response_processor import ResponseProcessor

class MessageMaker:
    def __init__(self, template='simple'):
        self.prompt_builder = PromptBuilder(template)
        self.gpt_client = GPTClient()
        self.response_processor = ResponseProcessor()

    def generate_message(self, changes, change_type, impact_area):
        prompt = self.prompt_builder.construct_prompt(changes, change_type, impact_area)
        raw_response = self.gpt_client.send_prompt(prompt)
        commit_message = self.response_processor.process_response(raw_response)
        return commit_message

    def regenerate_message(self, changes, feedback, change_type, impact_area):
        prompt = self.prompt_builder.construct_prompt(changes, change_type, impact_area, feedback)
        raw_response = self.gpt_client.send_prompt(prompt)
        commit_message = self.response_processor.process_response(raw_response)
        return commit_message
