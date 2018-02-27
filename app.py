
"""
Yuanchu Liu and Tiffany Moi
SoftDev2 pd7
K06 -- Ay Mon, Go Git It From Yer Flask
2018-02-26
"""

import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
import urllib2, json
from utils import db

app = Flask(__name__)

col = db.get_col()

#base 
@app.route("/")
def start():
    return render_template("home.html")

@app.route("/name", methods=['GET', 'POST'])
def name():
    form = request.args
    f_name = form['firstname']
    surname = form['surname']
    results = db.search_name(col, f_name, surname)
    return render_template("results.html", results = results)

@app.route("/birth", methods=['GET', 'POST'])
def birth():
    form = request.args
    country = form['country']
    results = db.search_birthCountry(col, country)
    return render_template("results.html", results = results)

@app.route("/death", methods=['GET', 'POST'])
def death():
    form = request.args
    country = form['country']
    results = db.search_deathCountry(col, country)
    return render_template("results.html", results = results)

@app.route("/category", methods=['GET', 'POST'])
def category():
    form = request.args
    cat = form['cat']
    results = db.search_category(col, cat)
    return render_template("results.html", results = results)

@app.route("/year", methods=['GET', 'POST'])
def year():
    form = request.args
    year = form['year']
    results = db.search_year_won(col, year)
    return render_template("results.html", results = results)


if __name__ == "__main__":
    
    app.debug = True
    app.run()
