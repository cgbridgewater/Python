from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)   
app.secret_key = 'mums the word'


@app.route("/")
def home_page():
    return render_template("index.html")



@app.route("/process")
def processing():
    return redirect("/result")



@app.route("/result")
def results():
    return render_template("result.html")



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

