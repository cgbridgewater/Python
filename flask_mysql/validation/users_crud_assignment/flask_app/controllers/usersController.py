from flask_app import app
from flask import redirect, render_template, request,session
from flask_app.models.users import User

### validations
@app.route('/register', methods=['POST'])
def create_user():
    # if there are errors:
    # We call the staticmethod on User model to validate
    if not User.validate_user(request.form):
        # redirect to the route where the user form is rendered.
        session["first_name"] = request.form["first_name"] ### HOLDING FORM DATA FOR RESUBMIT
        session["last_name"] = request.form["last_name"] ### HOLDING FORM DATA FOR RESUBMIT
        session["email"] = request.form["email"] ### HOLDING FORM DATA FOR RESUBMIT
        return redirect('/')
    # else no validation errors:
    User.logIn(request.form)
    session.pop("first_name")
    session.pop("last_name")
    session.pop("email")
    return redirect("/users")
### DEFAULT ROUTE (WORKING)
@app.route('/')
def home():
    return render_template('index.html')


### ROUTE TO ALL USERS - MAIN PAGE (WORKING)
@app.route('/users')
def index():
    return render_template("read(All).html", users = User.get_all())


### ROUTE TO NEW USER FORM (WORKING)
@app.route('/users/create')
def newUserForm():
    return render_template("create.html")


### ROUTE TO CREATE NEW USER AND DIRECT TO USER PROFILE PAGE (WORKING)
@app.route("/users/creating" , methods=['POST'])
def addUser():
    new_user_id = User.save(request.form)
    return redirect(f'/users/read/{new_user_id}')


### ROUTE TO VIEW USER PROFILE PAGE (WORKING)
@app.route('/users/read/<int:id>')
def showOneUser(id):
    data = {
    "id" : id
    }
    return render_template("read(one).html", user = User.get_one_user(data))


### ROUTE TO EDIT USER PROFILE (WORKING)
@app.route('/users/edit/<int:id>')
def editUser(id):
    data = {
    "id" : id
    }
    return render_template("edit.html", user = User.get_one_user(data))


### ROUTE TO UPDATE USER PROFILE AND REDIRECT TO USER PROFILE PAGE (WORKING)
@app.route('/users/updating/<int:id>', methods =['POST'])
def updateUser(id):
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id" : id
        }
    print('HELLO!!!!')
    User.updateUser(data)
    return redirect(f'/users/read/{id}') 


### ROUTE TO DELETE USER (WORKING)
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