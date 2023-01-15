from flask import make_response, render_template
import os, logging

def handle(request):
    try:
        print("Request inputs: {}".format(request.form))
        email = request.form["email"]
        print(email)
        resp = make_response(render_template('index.html'))
        resp.set_cookie("authorized", "True")
        return resp

    except:
        logging.exception("")

        print("failed")


