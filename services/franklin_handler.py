import os, logging
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def handle(request):
    try:
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt=generate_prompt(request.form),
        max_tokens=20,   
        temperature=0.6
        )
        return response.choices[0].text
    except:
        logging.exception('')
        print('failed')

def generate_prompt(form):
    return """Write a passionate real estate MLS listing description for a {} bedroom {} bathroom house in {}""".format(
        form['bedroom-count'],
        form['bathroom-count'],
        form['zipcode']
    )



class ChatGPT:
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


