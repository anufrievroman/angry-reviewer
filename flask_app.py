from flask import Flask, request, render_template
from processing import *

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def corrector_page():
    errors = ""
    text = None
    english = None
    if request.method == "POST":
        text = str(request.form["text"])
        text_split = text.split('\r\n')
        english = str(request.form.get("language"))
        results = main(text_split, english)
        return render_template('result.html', title="Angry Reviewer", results=results)
    return render_template('home.html', title="Angry Reviewer")


@app.route("/rules")
def rules_page():
    return render_template('rules.html', title='Rules')


@app.route("/about")
def about_page():
    return render_template('about.html', title='About')
