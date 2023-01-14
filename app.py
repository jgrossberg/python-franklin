import logging
from flask import Flask, redirect, render_template, request, url_for

import config
from services import franklin_handler

app = Flask(__name__)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        try:
            response = franklin_handler.handle(request)            
            return redirect(url_for("index", result=response))
        except:
            logging.exception('')
            print('failed')

            return redirect(url_for("index", result="error"))

    result = request.args.get("result")
    return render_template("index.html", checkboxes=config.checkboxes, result=result)
