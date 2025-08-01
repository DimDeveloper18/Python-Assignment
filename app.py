from flask import Flask, render_template, request

app = Flask(__name__)

calorie_table = {"Avocado": 1.6, "Artichoke": 0.5}

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/vegetables", methods=["GET", "POST"])
def veg_page():
    calories_total = ""
    if request.method == "POST":
        vegetable = request.form.get("vegetable")
        veg_gramm = request.form.get("gramm")
        gramm = float(veg_gramm)
        calories_total = round(gramm * calorie_table.get(vegetable, 0), 2)
    else:
            calories_total = "Invalid input"
    return render_template("vegetables.html", calories=calories_total)

@app.route("/meat")
def meat_page():
    return render_template("meat.html")

@app.route("/grains")
def grains_page():
    return render_template("grains.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")