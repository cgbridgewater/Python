from flask import render_template, request, redirect, session
from flask_app.models import user


@app.route('/allthethings')
    def allthethings():
        allUsers = user.User.getALL()
        print(allusers)
        return render_template('showquery.html')