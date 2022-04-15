#!/usr/bin/python3

# challenge: https://github.com/csfeeser/Python/blob/master/challenges/flask_challenge_jinja2.md
# builds on from flask_trivia.py

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)
# redirect here with answer
@app.route("/getresult/<answer>")
def getresult(answer):
    # render new template that determines correct or not using result
    return render_template("result.html", result = answer )

# This is a landing point for users (a start)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("postmaker.html") # look for templates/postmaker.html

# This is where postmaker.html POSTs data to
@app.route("/question", methods = ["POST"])
def question():
    if request.form.get("ans"):
        getans = request.form.get("ans")
        # redirect to getresult route with captured answer
        return redirect(url_for("getresult", answer = getans))
    else:
        return redirect("/")
    
    

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application