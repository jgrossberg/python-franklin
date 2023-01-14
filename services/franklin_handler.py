import os, logging
import openai



openai.api_key = os.getenv("OPENAI_API_KEY")


def handle(request):
    try:

        print("Request inputs: {}".format(request.form))
        print("Prompt: {}".format(generate_prompt(request.form)))
        
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(request.form),
            max_tokens=100,
            temperature=0.5,
        )
        print("Response: {}".format(response))
        return response.choices[0].text
    except:
        logging.exception("")

        print("failed")


def generate_prompt(form):
    if len(form["highlights"]) > 1:
        return """Write a passionate real estate MLS listing description for a {} bedroom {} bathroom house in {}. In the description, try to emphasize the house's {} and location (look up the city from the zip code).""".format(
            form["bedroom-count"], form["bathroom-count"], form["zipcode"], form["highlights"]
    )

    return """Write a passionate real estate MLS listing description for a {} bedroom {} bathroom house in {}.""".format(
            form["bedroom-count"], form["bathroom-count"], form["zipcode"])

