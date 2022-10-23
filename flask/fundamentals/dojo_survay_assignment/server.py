from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)   
app.secret_key = 'mums the word'

### Default route
@app.route("/")
def home_page():
    return render_template("index.html")

### Process and post route
@app.route("/process", methods = ['POST'])
def processing():
    session['name'] = request.form['name']
    session['dojoLocation'] = request.form ['dojoLocation']
    session['favLang'] = request.form['favLang']
    session['comment'] = request.form ['comment']
    session['spam'] = request.form ['spam']
    session['extraLanguage'] = request.form ['extraLanguage']
    return redirect("/result")

### Result Route
@app.route("/result")
def results():
    return render_template("result.html")

### DINO GAME CATCH ALL
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("dino_game.html")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

