import uuid

from flask import Flask, render_template, redirect, make_response, request

from services import franklin_handler, signup_handler

app = Flask(__name__)

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "GET":
        print("GET Request cookies: {}".format(request.cookies))

        resp = make_response(render_template("index.html"))
        queries = request.cookies.get('franklin-queries')
        if queries is None:
            resp.set_cookie('franklin-queries', '0')

        return resp
    elif request.method == "POST":
        print("POST Request cookies: {}".format(request.cookies))

        queries = int(request.cookies.get('franklin-queries'))
        if queries > 2:
            return redirect('/signup')
        
        response = make_response(render_template("index.html", result = franklin_handler.handle(request)))
        response.set_cookie('franklin-queries', str(queries + 1))
        return response

@app.route("/signup/", methods=("GET", "POST"))
def signup():
    if request.method == "GET":
        print("GET Request to /signup")
        return render_template("signup.html")
    elif request.method == "POST":
        print("POST Request to /signup")
        response = signup_handler.handle(request)
        return response

@app.route("/demo", methods=("GET", "POST"))
def limited_demo():
    print(request.cookies)
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        response = franklin_handler.handle(request)
        return render_template("index.html", result = response)

