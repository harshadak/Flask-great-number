from flask import Flask, render_template, request, redirect, session

import random

app = Flask(__name__)
app.secret_key = "Secret"

@app.route("/")
def index():
    message = ""
    print session
    if "guess_number" not in session:
        session["random_number"] = random.randrange(0, 101)
        print session
    elif session["guess_number"] < session["random_number"]:
        message = "low"
    elif session["guess_number"] > session["random_number"]:
        message = "high"
    elif session["guess_number"] == session["random_number"]:
        message = "correct"
        session.pop("guess_number")
        session.pop("random_number")
        session["random_number"] = random.randrange(0, 101)

    return render_template("index.html", message = message)

@app.route("/guess", methods = ["POST"])
def guess():
    session["guess_number"] = int(request.form["guess_key"])

    return redirect("/")

app.run(debug = True)