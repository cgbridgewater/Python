from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.users import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("login.html")


### ROUTE FOR REGISTRATION (CREATE USER)
@app.route('/register', methods= ['POST'])
def register():
    # We call the staticmethod on User model to validate
    if not User.validate_registration(request.form):
        session["first_name"] = request.form["first_name"] ### HOLDING FORM DATA FOR RESUBMIT
        session["last_name"] = request.form["last_name"] ### HOLDING FORM DATA FOR RESUBMIT
        session["email"] = request.form["email"] ### HOLDING FORM DATA FOR RESUBMIT
        return redirect('/')# redirect to the route where the user form is rendered if there are errors:
    pw_hash = bcrypt.generate_password_hash(request.form['password'])    ### hash password once validations are passed
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.save(data) ### save user
    session.pop("first_name", None)  ### clear form place holder sessions
    session.pop("last_name", None)   ### clear form place holder sessions
    session.pop("email", None)       ### clear form place holder sessions
    session['user_id'] = user_id     ### start user id session to prove logged in
    return redirect("/dashboard")    ### go to dashboard if no validation errors


### ROUTE FOR LOGIN
@app.route('/login', methods= ['POST'])
def login():
    # We call the staticmethod on User model to validate
    session["email2"] = request.form["email"] ### HOLDING FORM DATA FOR RESUBMIT
    data = { "email" : request.form["email"] }
    user_in_db = User.email_exists(data)
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not User.validate_login(request.form):
    # if there are errors:
        return redirect('/') # redirect to the route where the user form is rendered.
    # else no validation errors:
    session["user_id"] = user_in_db.id
    session.pop("email2", None)
    return redirect("/dashboard")


### ROUTE FOR LOGOUT 
@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")


### ROUTE FOR DASHBOARD READ BY USER_ID 
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html", user = User.get_user_by_id(data))


### ROUTE TO DELETE USER BY "ID" -- DRIVEN BY A BUTTON SUBMISSION OR SOMETHING (WORKING)
@app.route('/dashboard/delete')
def delete_user():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    User.delete_user(data)
    return redirect('/logout') 


    ### ROUTE TO EDIT USER FORM BY "ID" (WORKING)
@app.route('/dashboard/edit/')
def edit_user():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("edit.html", user = User.get_user_by_id(data))


### ROUTE TO UPDATE USER PROFILE (WORKING)
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


### ROUTE FOR FRIENDS PAGE 
@app.route('/dashboard/friends')
def all_users():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("user_friends.html", friends = User.get_friends(data),user = User.get_user_by_id(data)) ### This should be a joined list and all friends by id


### DINO GAME CATCH ALL (WORKING)
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("dinosaur.html")



### delete below this line when ready!

#######  EXAMPLE ROUTES

# ### ROUTE TO CREATE NEW USER AND DIRECT TO USER PROFILE PAGE BY "ID" -- FORM AND SUBMISSION REQUIRED!!! (WORKING)
# @app.route("/users/creating" , methods=['POST'])
# def addUser():
#     new_user_id = User.save(request.form)
#     return redirect(f'/users/read/{new_user_id}')



#     ### ROUTE TO VIEW USER PROFILE PAGE BY "ID" (WORKING)
# @app.route('/users/read/<int:id>')
# def show_one_user(id):
#     data = {
#     "id" : id
#     }
#     return render_template("read(one).html", user = User.get_one_user(data))




    
