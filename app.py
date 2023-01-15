from flask import Flask, render_template, request

from services import franklin_handler

app = Flask(__name__)

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        response = franklin_handler.handle(request)
        return render_template("index.html", result = response)

