# -*- coding: utf-8 -*-

import os

from uuid import uuid4

from flask import Flask, render_template, redirect, request, session
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

from tamuhackers19.db.firestore_client import FirestoreConnector
from tamuhackers19.user import User

import smartcar

app = Flask("tamuhack19")
app.secret_key = uuid4().hex

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

dbc = FirestoreConnector()


@app.route("/")
def home():
    return "Base template built successfully"


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_anonymous:
        if request.method == "POST":
            phone_number = request.args.phone_number
            if dbc.get_login_code(phone_number) == request.form["phone_number"]:
                user = User(phone_number)
                login_user(user)
                return redirect(url_for("/"))
        return render_template("login.html")
    return "You are already logged in!"


@app.route("/logout")
def logout():
    if not current_user.is_anonymous:
        logout_user()
        print("Logged out user.")
        return redirect(url_for("login"))
    print("There is no user available in the session.")
    return redirect(url_for("login"))

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    print(f"Initializing application on {host}:{port} ")
    app.run(host=host, port=port)