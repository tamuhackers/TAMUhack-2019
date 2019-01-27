from flask import Flask, render_template
import os

os.environ["FLASK_ENV"] = "development"

app = Flask("AccidentApp", template_folder=f"{os.path.dirname(os.path.realpath(__file__))}/templates")
@app.route("/", methods = ["GET"])
def home():
    return render_template("home.html")

@app.route("/profile", methods = ["GET"])
def profile():
    return render_template("profile.html")

@app.route("/emergency", methods = ["GET"])
def emergency():
    return render_template("emergency.html")

@app.route("/light", methods = ["GET"])
def light():
    return render_template("light.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5001)