  
# =========================================================
# IMPORT ALL RELEVANT MODULES
# =========================================================

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars



app = Flask(__name__)



# =========================================================
# USE flask_pymongo TO SET UP A MONGO CONNECTION
# =========================================================

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)



# =========================================================
# CREATE AN APP ROUTE FOR THE HOME PAGE
# =========================================================

@app.route("/")
def index():
    marspage = mongo.db.marspages.find_one()
    return render_template("index.html", marspage=marspage)



# =========================================================
# CREATE AN APP ROUTE FOR THE SCRAPING FUNCTIONALITY
# =========================================================

@app.route("/scrape")
def scraper():
    marspages = mongo.db.marspages
    marspagedata = scrape_mars.scrape()
    marspages.update({}, marspagedata, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)