import os
import config

from flask import Flask, redirect, render_template, request, url_for

import open_ai_service

app = Flask(__name__)



@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        bedroom_count = request.form["bedroom-count"]
        bathroom_count = request.form["bathroom-count"]
        try:
            print(os.getenv("OPEN_API_KEY"))
            service = open_ai_service.OpenAiService(os.getenv("OPENAI_API_KEY"))
            response = service.create_completion(generate_prompt(bedroom_count))
            
            return redirect(url_for("index", result=response))
        except:
            return redirect(url_for("index", result="error"))

    result = request.args.get("result")
    return render_template("index.html", checkboxes=config.checkboxes, result=result)


def generate_prompt(bedroom_count):
    return """Write the real estate MLS listing description for the following property: 
    
    bedroom count: {}

    """.format(
        bedroom_count
    )
