from typing import Counter
from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)   
app.secret_key = 'mums the word'


### Home
@app.route('/')
def setNumber():
    if 'randomNum' not in session:
        session['randomNum'] = random.randint(1,5)
    if 'guesses' not in session:
        session['guesses'] = 0
    return render_template('index.html')


### guessed number
@app.route('/guess', methods = ['POST'])
def guessNumber():
    session['guess'] = int(request.form['guess'])
    print(session['guess'])
    print(session['randomNum'])
    session['guesses'] +=1
    print(session['guesses'])
    return redirect("/")


### name input for leader board
@app.route('/names', methods = ['POST'])
def getNames():
    session['first_name'] = request.form['first_name']
    session['attempts'] = request.form['attempts']
    return redirect('/leaderboard')


### leaderboard display
@app.route('/leaderboard')
def leaders():
    return render_template('leaderboard.html')


### reset sessions
@app.route('/reset')
def resetGame():
    session.pop('randomNum')
    session.pop('guess')
    session.pop('guesses')
    return redirect("/")


### reset everything including leaderboard
@app.route('/clear')
def clearAll():
    session.clear()
    return redirect("/")


### DINO GAME CATCH ALL
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("dino_game.html")


### DEBUGGING
if __name__=="__main__":   
    app.run(debug=True) 