import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
import urllib2, json

app = Flask(__name__)


#base 
@app.route("/")
def start():
    return 
    


if __name__ == "__main__":
    app.debug = True
    app.run()