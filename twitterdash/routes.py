from flask import Flask, render_template, request
import pandas as pd
from textblob import TextBlob


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("landing.html")
