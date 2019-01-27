import os

from flask import Flask, redirect, url_for, render_template, request
from tamuhackers19.db.firestore_client import FirestoreConnector

app = Flask(__name__)
dbc = FirestoreConnector()

@app.route("/")
def send_email():
	

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    print(f"Initializing application on {host}:{port} ")
    app.run(host=host, port=port)