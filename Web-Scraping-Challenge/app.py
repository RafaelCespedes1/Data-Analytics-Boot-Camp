from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

 # Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")


@app.route('/')
def index():
    listings = mongo.db.mars.find_one()
    return render_template("index.html", data=listings)
 

@app.route("/scrape")
def scrape():
    marsdb = mongo.db.mars
    mars_scrape = scrape_mars.scrape()

    marsdb.update({}, mars_scrape, upsert=True)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True) 
