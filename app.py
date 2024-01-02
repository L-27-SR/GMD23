import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///details.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    nuclear_data = db.execute("select * from nuclear")
    return render_template("index.html", nuclear = nuclear_data)

@app.route("/airforce")
def airforce():
    air_data = db.execute("select * from air")
    return render_template("airforce.html", air_data = air_data)

@app.route("/army")
def army():
    army_data = db.execute("select * from arm")
    return render_template("army.html", army_data = army_data)

@app.route("/navy")
def navy():
    naval_data = db.execute("select * from navy")
    return render_template("navy.html", naval_data = naval_data)
