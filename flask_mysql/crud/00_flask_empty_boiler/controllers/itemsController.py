from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import user


@app.route('/')
def index():
    return render_template("index.html")

