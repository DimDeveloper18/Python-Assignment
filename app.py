from flask import Flask, render_template, request

app = Flask(__name__)

veg_cal_table = {"Avocado": 1.6, "Artichoke": 0.5, "Asian greens": 0.3, "Asparagus": 0.1, "Beetroot": 3, "Broad beans": 0.3, "Broccoli": 0.4, "Broccolini": 0.4, "Brussel sprouts": 0.7, "Butternut pumpkin": 0.8, "Cabbage": 1, "Capsicum": 0.3, "Carrot": 0.8, "Cauliflower": 0.5, "Celery": 0.9,}

meat_cal_table = {"Pork": 3, "Beef": 2.5, "Veal": 1.8, "Mutton": 1.5, "Lamb": 3, "Goat Meat": 2.8, "Venison": 5.4, "Bison Meat": 6.4, "Kangaroo Meat": 7, "Game Meats": 5.8, "Chicken": 1, "Duck": 2.3, "Türkiye": 1, "Goose": 0.5, "Pheasant": 1.8,}

grain_cal_table = {"Barley": 0.3, "Bulgur": 1.5, "Farro": 1.8, "Millet": 1.5, "Quinoa": 0.3, "Black rice": 0.8, "Red rice": 0.4, "Wild rice": 1.4, "Oatmeal": 0.7, "Popcorn": 1.8, "Whole-wheat flour": 1, "Whole-grain cereals": 2.3, "Whole-wheat bread": 2.1, "Pasta": 2.5, "Crackers": 1.8,}

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/vegetables", methods=["GET", "POST"])
def veg_page():
    veg_cal_total = ""
    if request.method == "POST":
        vegetable = request.form.get("vegetable")
        veg_gramm = request.form.get("gramm")
        gramm = float(veg_gramm)
        veg_cal_total = round(gramm * veg_cal_table.get(vegetable, 0), 2)
    else:
        veg_cal_total = "Invalid input"
    return render_template("vegetables.html", calories=veg_cal_total)

@app.route("/meat", methods=["GET", "POST"])
def meat_page():
    meat_cal_total = ""
    if request.method == "POST":
        meat = request.form.get("meat")
        veg_gramm = request.form.get("gramm")
        gramm = float(veg_gramm)
        meat_cal_total = round(gramm * meat_cal_table.get(meat, 0), 2)
    else:
        meat_cal_total = "Invalid input"
    return render_template("meat.html", calories=meat_cal_total)

@app.route("/grains", methods=["GET", "POST"])
def grains_page():
    grain_cal_total = ""
    if request.method == "POST":
        grain = request.form.get("grain")
        veg_gramm = request.form.get("gramm")
        gramm = float(veg_gramm)
        grain_cal_total = round(gramm * grain_cal_table.get(grain, 0), 2)
    else:
        grain_cal_total = "Invalid input"
    return render_template("grains.html", calories=grain_cal_total)

@app.route("/contact")
def contact_page():
    return render_template("contact.html")