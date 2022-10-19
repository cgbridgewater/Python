from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)   
app.secret_key = 'mums the word'

### DO I EVEN NEED THIS??  DEFAULT PAGE
@app.route('/')
def index():
    return redirect("/home")

### HOME PAGE - THIS IS WHERE THE MAGIC HAPPENS
@app.route('/home', methods = ['GET'])
def home():
    print('WELCOME HOME!')
### IF STATEMENT FOR COUNTER IN SESSION
    if not 'counter' in session:
        session['counter'] =0        
        session['hits'] =0
        print('counter isnt moving')
    else:
        session['counter'] += 1
        print('counters going')
### IF STATEMENT FOR HITS IN SESSION
    if not 'hits' in session:
        session['hits'] =0
        print('counter isnt moving')
    else:
        session['hits'] += 1
        print('counters going')
    return render_template("index.html")

### SINGLE UP COUNTER
@app.route('/plusone')
def plus_one():
    print('ONE ADDED TO THE COUNTER!!! ')
    return redirect("/home")

### ADDS TWO HITS ONTO THE SITE HITS
@app.route('/plustwo')
def plus_two():
    print('TWO ADDED TO THE COUNTER!!! ')
    session['counter'] +=1
    return redirect("/home")

### RESETS SITE VISITS COUNTER
@app.route('/clear')
def clear_session():
    print('COUNTER CLEARED!!!')
    session['counter'] =0
    return redirect("/home")

### ENDS SESSION AND RESETS COUNTERS TO ZERO
@app.route('/destroy')
def destroy_session():
    print('SESSION ENDED!!!')
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

