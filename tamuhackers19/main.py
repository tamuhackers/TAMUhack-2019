# -*- coding: utf-8 -*-

import os

from flask import Flask, render_template, redirect

import smartcar

app = Flask("tamuhack19")

@app.route("/")
def home():
    return "Base template built successfully"
    
if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    print(f"Initializing application on {host}:{port} ")
    app.run(host=host, port=port)