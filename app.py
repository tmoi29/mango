import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
import urllib2, json
from utils import db

app = Flask(__name__)

#base 
@app.route("/")
def start():
    return render_template("home.html")

@app.route("/results")
def results():
    
    return render_template("results.html")


if __name__ == "__main__":
    
    app.debug = True
    app.run()
