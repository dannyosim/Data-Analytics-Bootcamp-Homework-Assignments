from flask_pymongo import pymongo
from flask import Flask, render_template
import scrape_mars

app=Flask(__name__)

app.config["MONGO_URI"]="mongodb://localhost:27017/DannyMars"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.collection1.find_one()
    return render_template("index.html)


@app.route("/scrape")
def scrape():
    mars = mongo.db.collection1
    mars_data = scrape_mars.AllData()
    
return mars.update({}, mars_data, upsert=True)
    


if __name__ == "__main__":
    app.run(debug=True)
