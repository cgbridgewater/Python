from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.users import User
from flask_app.models.rides import Ride


### ROUTE FOR DASHBOARD -- READ BY USER_ID  (WORKING)
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html", user = User.get_user_by_id(data), rideshares = Ride.get_all_users_and_rides())


    ### ROUTE TO USER UPDATE FORM BY USER_ID (WORKING)
@app.route('/dashboard/edit/')
def edit_user():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("edit.html", user = User.get_user_by_id(data))


    ### ROUTE TO PROCESS USER UPDATE FORM (WORKING)
@app.route("/dashboard/editing", methods =['POST'])
def update_user():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : session['user_id'],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
        }
    if not User.validate_update(data):
        return redirect('/dashboard/edit/')
    User.update_user_by_id(data)
    return redirect("/dashboard") 


    ### ROUTE TO DELETE USER BY USER_ID (WORKING)
@app.route('/dashboard/delete')
def delete_user():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    User.delete_user(data)
    return redirect('/logout')