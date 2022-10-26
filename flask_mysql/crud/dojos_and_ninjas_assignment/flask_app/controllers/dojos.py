from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo 
from flask_app.models.ninja import Ninja




### ROUTE TO REDIRECT TO DOJO HOME (WORKING)
@app.route('/')
def index():
    return redirect("/dojos")


### ROUTE TO DOJO HOME and FETCHING DOJO DATA (WORKING)
@app.route('/dojos')
def home():
    return render_template("index.html", dojos = Dojo.get_all())



### ROUTE TO CREATE NEW DOJO AND DIRECT TO DOJO HOME (WORKING)
@app.route("/dojos/create" , methods=['POST'])
def addUser():
    Dojo.create(request.form)
    return redirect('/dojos')



### ROUTE TO VIEW USER PROFILE PAGE BY "ID" (NOT WORKING)
@app.route('/dojos/<int:id>')
def showOneDojo(id):
    data = {
    "id" : id
    }
    return render_template("dojo(one).html", one_dojo = Dojo.getDojoAndNinjas(data))







### DINO GAME CATCH ALL (WORKING)
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("dinosaur.html")
