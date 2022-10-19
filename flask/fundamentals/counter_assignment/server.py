from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)   
app.secret_key = 'mums the word'

### DO I EVEN NEED THIS??  FORWARDS TO DEFAULT HOME PAGE
@app.route('/')
def index():
    return redirect("/home")

### HOME PAGE - THIS IS WHERE THE MAGIC HAPPENS
@app.route('/home', methods = ['GET'])
def home():
### IF STATEMENT FOR COUNTER IN SESSION
    if not 'counter' in session:
        session['counter'] =0        
        session['hits'] =0
    else:
        session['counter'] += 1
### IF STATEMENT FOR HITS IN SESSION
    if not 'hits' in session:
        session['hits'] =0
    else:
        session['hits'] += 1
    return render_template("index.html")

### SINGLE UP COUNTER
@app.route('/plusone')
def plus_one():
    return redirect("/home")

### ADDS TWO HITS ONTO THE SITE HITS
@app.route('/plustwo')
def plus_two():
    session['counter'] +=1
    return redirect("/home")

### ADD ON - ADDS ON 'X' NUMBER TO THE SESSION COUNTER
@app.route('/addon', methods = ['POST'])
def add_on():
    session['nums'] = request.form['nums']
    session['counter'] += int(session['nums'])-1
    return redirect("/home")

### RESETS SITE VISITS COUNTER
@app.route('/clear')
def clear_session():
    session['counter'] =0
    return redirect("/home")

### ENDS SESSION AND RESETS COUNTERS TO ZERO
@app.route('/destroy')
def destroy_session():
    session.clear()
    session['counter'] =0
    session['hits'] =0
    return redirect("/home")

### DINO GAME CATCH ALL
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("dino_game.html")

### DEBUGGING
if __name__=="__main__":   
    app.run(debug=True) 