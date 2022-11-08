from pprint import pprint
from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.recipe import Recipe
from flask_app.models.users import User


### ROUTE TO CREATE NEW RECIPE PAGE (WORKING)
@app.route("/recipe/create")
def create_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("new_recipe.html")


### ROUTE TO POST NEW RECIPE FORM AND DIRECT TO DASHBOARD (WORKING)
@app.route("/recipe/creating" , methods=['POST'])
def add_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipe/create')   # redirect to the route where the Order form is rendered.
    Recipe.save_recipe(request.form)   # else no validation errors:
    return redirect("/dashboard")


    ###ROUTE TO READ SINGLE RECIPE (WORKING)
@app.route('/recipe/view/<int:id>/<int:user_id>')
def view_recipe(id,user_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': id,
        'user_id' : user_id
    }
    id = {
    "id" : session['user_id']
    }
    return render_template("view_recipe.html", recipe = Recipe.get_one_recipe_and_user(data), user = User.get_user_by_id(id))


    ## ROUTE TO UPDATE RECIPE FORM BY ID (WORKING)
@app.route('/recipe/edit/<int:id>')
def get_one_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': id
    }
    return render_template("edit_recipe.html", recipe = Recipe.get_one_recipe(data))


### ROUTE TO POST RECIPE UPDATE FORM (WORKING)
@app.route("/recipe/editing", methods =['POST'])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        session["id"] = request.form["id"] ### HOLDING FORM DATA FOR RESUBMIT
        # redirect to the route where the Order form is rendered.
        return redirect(f'/recipe/edit/{session["id"]}')
    # else no validation errors:
    Recipe.update_recipe(request.form)
    session.pop("id", None)
    return redirect("/dashboard") 


### ROUTE TO DELETE RECIPE (WORKING)
@app.route('/recipe/delete/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': id
    }
    Recipe.delete_recipe(data)
    return redirect("/dashboard") 