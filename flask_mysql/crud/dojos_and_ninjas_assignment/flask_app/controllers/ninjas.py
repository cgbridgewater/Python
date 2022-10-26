from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


### ROUTE TO DIRECT TO ADD Ninja page HOME (WORKING)
@app.route("/dojos/ninjas")
def ninjaPage():
    all_dojos = Dojo.get_all()
    return render_template('ninjas.html', all_the_dojos= all_dojos)

### ROUTE TO CREATE NEW DOJO AND DIRECT TO DOJO HOME (WORKING)
@app.route("/dojos/ninjas/create" , methods=['POST'])
def addNinja():
    print(request.form)
    dojo_id = request.form["dojo_id"]
    return redirect(f'/dojos/{dojo_id}')


# ### ROUTE TO GO HOME
# @app.route("/dojos")
# def goHome():
#     return render_template("index.html")