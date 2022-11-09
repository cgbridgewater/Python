from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.users import User
from flask_app.models.rides import Ride


### works
@app.route('/ride/new')
def ride_form():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data = {
        'id' : session['user_id']
    }
    return render_template("new_ride.html", user = User.get_user_by_id(data))


### works
@app.route("/ride/creating", methods = (["POST"]))
def ride_post():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data = {
        'rider_id': session['user_id'],
        "destination" : request.form['destination'],
        "pick_up" : request.form['pick_up'],
        "date" : request.form['date'],
        "details" : request.form['details'],
        }     
    if not Ride.validate_form(data):
        session["destination"] = request.form['destination']       
        session["pick_up"] = request.form['pick_up']
        session["details"] = request.form['details']
        return redirect('/ride/new')
    Ride.save_ride(data)
    print(data)
    session.pop('destination',None)
    session.pop('pick_up',None)
    session.pop('detials',None)
    return redirect("/dashboard")


### works
@app.route('/ride/update/<int:id>')
def update_form(id):
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data = {
        'id' : id
    }
    return render_template("update_ride.html",  ride = Ride.get_ride_by_id(data))


### works
@app.route('/ride/drive/<int:id>')
def accept_ride(id):
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data = {
        'id' : id,
        'driver_id' : session['user_id']
    }
    Ride.accept_ride(data)
    return redirect("/dashboard" )


### works
@app.route('/ride/cancel/<int:id>')
def cancel_ride(id):
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data = {
        'id' : id,
        # 'driver_id' : "NULL"
    }
    Ride.cancel_ride(data)
    return redirect("/dashboard" )


### works
@app.route("/ride/updating", methods = (["POST"]))
def ride_update():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data = {
        'id': request.form['id'],
        "pick_up" : request.form['pick_up'],
        "details" : request.form['details'],
        }  
    print(data)   
    if not Ride.validate_update(data):
        session['id'] = request.form['id']
        session["pick_up"] = request.form['pick_up']
        session["details"] = request.form['details']
        return redirect(f'/ride/update/{session["id"]}')
    Ride.update_ride(data)
    print(data)
    session.pop('pick_up', None)
    session.pop('detials', None)
    session.pop('id', None)
    return redirect("/dashboard")


    ### ROUTE TO DELETE RIDE BY RIDE_ID (WORKING)
@app.route('/ride/delete/<int:id>')
def delete_ride(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': id
    }
    Ride.delete_ride(data)
    return redirect('/dashboard') 