import logging, os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAiService:
    url = 'https://api.openai.com/v1/completions'        

    def create_completion(self, prompt):
        try:
            response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            max_tokens=10,   
            temperature=0.6
            )
            return response.choices[0].text
        except:
            logging.exception('')
            print('failed')


