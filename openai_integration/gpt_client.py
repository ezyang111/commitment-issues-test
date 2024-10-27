# openai_integration/gpt_client.py

import openai
import os
import time
import logging

class GPTClient:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model = "gpt-4o-mini"  # Ensure this is the correct model name
        self.max_retries = 3
        self.retry_delay = 2  # seconds

    def send_prompt(self, prompt):
        for attempt in range(1, self.max_retries + 1):
            try:
                response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": prompt}
                    ],
                    max_tokens=2000,
                )
                return response.choices[0].message["content"].strip()
            except openai.error.RateLimitError:
                logging.warning(f"Rate limit exceeded. Retrying in {self.retry_delay} seconds...")
                time.sleep(self.retry_delay)
            except openai.error.OpenAIError as e:
                logging.error(f"OpenAI API error: {e}")
                break
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                break
        return None
