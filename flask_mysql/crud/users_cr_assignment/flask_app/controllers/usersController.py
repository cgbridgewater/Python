from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.users import User


@app.route('/')
def home():
    return redirect('/users')


@app.route('/users')
def index():
    return render_template("readAll.html", users = User.get_all())


@app.route('/users/create')
def newUserForm():
    return render_template("create.html")


@app.route("/users/creating" , methods=['POST'])
def addUser():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

### DINO GAME CATCH ALL
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("dinosaur.html")