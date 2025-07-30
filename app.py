from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/vegetables")
def veg_page():
    return render_template("vegetables.html")

@app.route("/meat")
def meat_page():
    return render_template("meat.html")

@app.route("/grains")
def grains_page():
    return render_template("grains.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")