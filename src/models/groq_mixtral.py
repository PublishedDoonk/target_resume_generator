from src.models.base_classes import LanguageModel
from groq import Groq
import json
import re

class GroqMixtral(LanguageModel):
    def __init__(self, instructions: str, sample_outputs: list | None = None, schema: dict | None = None, prev_messages: list | None = None):
        super().__init__(instructions, sample_outputs, schema, prev_messages)
        API_KEY = self.import_key_from_keyring('GROQ_API')
        self.client = Groq(
            api_key=API_KEY
        )
    
    def prompt_model(self, prompt: str):
        prompt = [{'role': 'user', 'content': prompt}]
        completion = self.client.chat.completions.create(
            messages=self.instructions + self.prev_messages + prompt,
            model='mixtral-8x7b-32768',
            temperature=0.5,
        )
        resp = completion.choices[0].message.content
        if self.schema and (json_substring := re.search(r'{.*}', resp, re.DOTALL)):
            resp = json_substring.group(0)
        msg = [{'role': 'assistant', 'content': resp}]
        self.prev_messages = self.prev_messages + prompt + msg
        if self.schema:
            return json.loads(resp)
        return resp