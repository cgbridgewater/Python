from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.users import User

### REDIRECT TO USERS PAGE
@app.route('/')
def index():
    return redirect("/users")


### ROUTE TO VIEW ALL USERS (WORKING)
@app.route('/users')
def showAll():
    return render_template("index.html", users = User.get_all(), friends = User.getFriends())


### ROUTE TO CREATE NEW USER (WORKING)
@app.route("/users/create" , methods=['POST'])
def addUser():
    User.saveUser(request.form)
    return redirect(f'/users')


### ROUTE TO CREATE A NEW FRIENDSHIP (WORKING)
@app.route("/users/friends", methods=['POST'])
def makeFriendship():
    User.saveFriendship(request.form)
    return redirect("/users")






##### below is not used yet


    ### ROUTE TO EDIT USER PROFILE BY "ID" (testing)
@app.route('/users/edit/<int:id>')
def editUser(id):
    data = {
    "id" : id
    }
    return render_template("edit.html", user = User.get_one_user(data))



### ROUTE TO UPDATE USER PROFILE AND REDIRECT TO USER PROFILE PAGE BY "ID" -- FORM AND SUBMISSION REQUIRED!!! (testing)
@app.route('/users/updating/<int:id>', methods =['POST'])
def updateUser(id):
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "id" : id
        }
    print('HELLO!!!!')
    User.updateUser(data)
    return redirect(f'/users/read/{id}') 


    
### ROUTE TO DELETE USER BY "ID" -- DRIVEN BY A BUTTON SUBMISSION OR SOMETHING (testing)
@app.route('/users/delete/<int:id>')
def deleteUser(id):
    data = {
    "id" : id
    }
    User.deleteUser(data)
    return redirect('/users') 




### DINO GAME CATCH ALL (WORKING)
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("dinosaur.html")
