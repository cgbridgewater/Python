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
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.save(data)
    session.pop("first_name", None)
    session.pop("last_name", None)
    session.pop("email", None)
    session['user_id'] = user_id
    # else no validation errors:
    return redirect("/dashboard")


### ROUTE FOR LOGIN
@app.route('/login', methods= ['POST'])
def login():
    # We call the staticmethod on User model to validate
    data = { "email" : request.form["email"] }
    user_in_db = User.email_exists(data)
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not User.validate_login(request.form):
        session["email"] = request.form["email"] ### HOLDING FORM DATA FOR RESUBMIT
    # if there are errors:
        return redirect('/') # redirect to the route where the user form is rendered.
    # else no validation errors:
    session["user_id"] = user_in_db.id
    session.pop("email", None)
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


######  check and make these funcitonal !!!!!!   ensure session is working and controls the page data!!!

    ### ROUTE TO EDIT USER FORM BY "ID" (WORKING)
@app.route('/users/edit/<int:id>')
def edit_user(id):
    data = {
    "id" : id
    }
    return render_template("edit.html", user = User.get_user_by_id(data))


### ROUTE TO UPDATE USER PROFILE AND REDIRECT TO USER PROFILE PAGE BY "ID" (WORKING)
@app.route('/users/updating/<int:id>', methods =['POST'])
def update_user(id):
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id" : id
        }
    print('HELLO!!!!')
    User.updateUser(data)
    return redirect(f'/users/read/{id}') 



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




    
