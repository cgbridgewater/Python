from flask_app import app
from flask import render_template, request, redirect,session
from flask_app.models.cookies import Order


### DIRECT TO HOME
@app.route('/')
def index():
    return redirect("/cookies")


### HOME PAGE
@app.route('/cookies')
def home():
    return render_template("cookies.html", cookies = Order.getAllOrders())


### ROUTE TO NEW ORDERS PAGE
@app.route("/cookies/new")
def newOrder():
    return render_template("new_cookies.html")


### ROUTE TO CREATE NEW ORDER  (WORKS)
@app.route("/cookies/new/add" , methods=['POST'])
def addOrder():
    # if there are errors: we call the @staticmethod on Order model to validate
    if not Order.validateOrder(request.form):
        # redirect to the route where the Order form is rendered.
        session["customer_name"] = request.form["customer_name"] ### HOLDING FORM DATA FOR RESUBMIT
        session["cookie_type"] = request.form["cookie_type"] ### HOLDING FORM DATA FOR RESUBMIT
        session["boxes"] = request.form["boxes"] ### HOLDING FORM DATA FOR RESUBMIT
        return redirect('/cookies/new')
    # else no validation errors:
    Order.saveOrder(request.form)
    session.pop("customer_name", None)  ### POPPING FORM DATA FOR RESUBMIT
    session.pop("cookie_type", None)  ### POPPING FORM DATA FOR RESUBMIT
    session.pop("boxes", None)  ### POPPING FORM DATA FOR RESUBMIT
    return redirect('/cookies')


    ### ROUTE TO EDIT ORDER  BY "ID" (WORKS)
@app.route('/cookies/edit/<int:id>')
def editUser(id):
    data = {
    "id" : id
    }
    return render_template("edit_cookies.html", order = Order.getByOrderId(data))


### ROUTE TO UPDATE USER PROFILE AND REDIRECT TO USER PROFILE PAGE BY "ID" -- FORM AND SUBMISSION REQUIRED!!! (WORKS)
@app.route('/cookies/editing', methods =['POST'])
def updateUser():
    # if there are errors: we call the staticmethod on Order model to validate
    if not Order.validateOrder(request.form):
        print("A")
        print("A")
        print(request.form)
        # redirect to the route where the order form is rendered.
        id = request.form["id"]
        session["id"] = request.form["id"]
        session["customer_name"] = request.form["customer_name"] ### HOLDING FORM DATA FOR RESUBMIT
        session["cookie_type"] = request.form["cookie_type"] ### HOLDING FORM DATA FOR RESUBMIT
        session["boxes"] = request.form["boxes"] ### HOLDING FORM DATA FOR RESUBMIT
        return redirect(f'/cookies/edit/{session["id"]}')
    # else no validation errors:
    Order.updateOrder(request.form)
    session.pop("customer_name",None)  ### POPPING FORM DATA FOR RESUBMIT
    session.pop("cookie_type", None)  ### POPPING FORM DATA FOR RESUBMIT
    session.pop("boxes", None)  ### POPPING FORM DATA FOR RESUBMIT
    return redirect('/cookies') 


### ROUTE TO DELETE ORDER BY "ID" (WORKS)
@app.route('/cookies/delete/<int:id>')
def deleteOrder(id):
    data = {
    "id" : id
    }
    Order.deleteOrder(data)
    return redirect('/cookies') 


### DINO GAME CATCH ALL (WORKS)
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("dinosaur.html")
