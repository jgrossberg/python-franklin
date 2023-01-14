import os, logging
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def handle(request):
    try:

        bedroom_count = request.form["bedroom-count"]
        bathroom_count = request.form["bathroom-count"]

        response = openai.Completion.create(
        model="text-davinci-002",
        prompt=generate_prompt(bedroom_count),
        max_tokens=10,   
        temperature=0.6
        )
        return response.choices[0].text
    except:
        logging.exception('')
        print('failed')

def generate_prompt(bedroom_count):
    return """Write the real estate MLS listing description for the following property: 
    
    bedroom count: {}

    """.format(
        bedroom_count
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


