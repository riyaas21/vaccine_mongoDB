from flask import Flask, render_template, request
import requests
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://database-service:27017", username="riyaas", password="password")

db = client["vaccination"]

collection = db["vaccination_status"]

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/vaccination_status", methods=["POST"])
def vaccination_status():
    reg_no = request.form["reg_no"]

    reg_no = str(reg_no)

    res_data = collection.find_one({"reg_no": reg_no})

    print(res_data, reg_no)

    if not res_data:
        return render_template("home.html", status="Not Found")

    if res_data["vaccination_status"]:

        return render_template("home.html", status="Vaccinated")


    return render_template("home.html", status="Not Vaccinated")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
