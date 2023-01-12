import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        bedroom_count = request.form["bedroomCount"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(bedroom_count),
            max_tokens=500,   
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(bedroom_count):
    return """Write the real estate MLS listing description for the following property: 
    
    bedroom count: {}

    """.format(
        bedroom_count
    )
