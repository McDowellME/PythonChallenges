#!/usr/bin/python3

# challenge: https://github.com/csfeeser/Python/blob/master/challenges/FLASK_challenge.md

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)
## This is where we want to redirect users to
@app.route("/correct")
def correct():
    return "Correct!\n"
    
# @app.route("/incorrect/<name>")
# def incorrect(name):
#     return f"{name} is incorrect. Try again\n"

# This is a landing point for users (a start)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("postmaker.html") # look for templates/postmaker.html

# This is where postmaker.html POSTs data to
@app.route("/question", methods = ["POST"])
def question():
    answer = request.form.get("ans")
    if answer == "12": # if ans was correct, redirect to "correct"
        result = "correct"
    else: # return to form
        result = "start"
    
    return redirect(url_for(result)) # redirect based on result

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application