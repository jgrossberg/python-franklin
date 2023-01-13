import logging

import requests

class OpenAiService:
    def __init__(self, api_key):
        self.api_key = api_key

        self.url = 'https://api.openai.com/v1/completions'

    def create_completion(self, prompt):
        try:
            print('completion with prompt')
            payload = {
                'model': 'text-davinci-003',
                'prompt': prompt,
                'temperature': .6,
                'max_tokens': 10
            }

            headers = {"Authorization": "Bearer " + str(self.api_key)}

            r = requests.post(self.url, json=payload, headers=headers)
            print(r.text)
            print(r.json())
            return r.json()['choices'][0]['text']
        except:
            logging.exception('')
            print('failed')


