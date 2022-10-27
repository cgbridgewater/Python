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
def create():
    Ninja.addNinja(request.form)
    dojo_id = request.form["dojo_id"]
    return redirect(f'/dojos/{dojo_id}')


# ### ROUTE TO GO TO NINJA EDIT PAGE ( WORKING)   POTENTIAL REPLACE!
# @app.route('/dojos/ninjas/edit/<int:dojo_id>/<int:id>')
# def editUser(id,dojo_id):
#     data = {
#     "id" : id,
#     "dojo.id" : dojo_id
#     }
#     return render_template("edit.html", ninja = Ninja.getOneNinja(data))


### ROUTE TO GO TO NINJA EDIT PAGE (Testing) (THIS WORKS!!!)
@app.route('/dojos/ninjas/edit/<int:dojo_id>/<int:id>')
def editUser(id, dojo_id):
    data = {
    "id" : id,
    "dojo_id" : dojo_id
    }
    return render_template("edit.html", dojo_id= dojo_id, ninja = Ninja.getOneNinja(data))






## NOT working
@app.route("/dojos/ninjas/update/<int:dojo_id>" , methods = ['POST'])
def updateNinja(dojo_id):
    data = {
    "first_name": request.form["first_name"],
    "last_name": request.form["last_name"],
    "age": request.form["age"],
    "id" : request.form["id"],
    "dojo_id" : dojo_id
    }
    print('UPDATING NINJA INFO')
    Ninja.updateNinja(data)
    return redirect(f'/dojos/{dojo_id}')

    # return render_template("/dojos(one)", Dojo.getDojoAndNinjas(data))




# ### ROUTE TO UPDATE USER PROFILE AND REDIRECT TO USER PROFILE PAGE (WORKING)
# @app.route("/dojos/ninjas/update<int:id>", methods =['POST'])
# def updateUser(id, dojo_id):
#     data = {
#         "first_name": request.form["first_name"],
#         "last_name": request.form["last_name"],
#         "email": request.form["email"],
#         "id" : id,
#         "dojo_id" : dojo_id
#         }
#     print('HELLO!!!!')

#     return render_template("dojo(one).html", one_dojo = Dojo.getDojoAndNinjas(data))



#     return redirect(f'/users/read/{id}') 
# one_dojo = Dojo.getDojoAndNinjas(data)










### ROUTE TO DELETE NINJA AND REDIRECT BACK TO DOJO (WORKING!)
@app.route('/dojos/ninjas/delete/<int:dojo_id>/<int:id>')
def deleteNinja(id, dojo_id):
    data = {
    "id" : id,
    "dojo_id" : dojo_id
    }
    Ninja.deleteNinja(data)
    return redirect(f'/dojos/{dojo_id}')
