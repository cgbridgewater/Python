from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)  
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes



@app.route('/')
def index():
    return render_template("index.html")



@app.route('/users', methods = ['POST'])         
def create_user():
    print("Got Post Info")
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form ['email']
    return redirect("/checkout")




@app.route('/checkout')         
def checkout():

    return render_template("checkout.html")
    #  , last_name = lastName, email = student_id)








@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    