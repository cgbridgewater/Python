from flask import Flask, render_template, request  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


#HOME PAGE
@app.route('/')          
def hello_world():
    return render_template('index.html')

#PLAY PAGE WITH STACKED INPUT OPTIONS
@app.route('/play/', endpoint='play')
@app.route('/play/<int:num>/', endpoint='<int:num>')
@app.route('/play/<int:num>/<string:color>/', endpoint='<int:num>/<string:color>')
def play(num=None,color=None): 
    if request.endpoint == '/play':
        return render_template("play.html")    
    if request.endpoint == '<int:num>':
        return render_template("play.html", num=3 )
    if request.endpoint == '<int:num>/<string:color>':
        return render_template("play.html", num=3, color = color )    
    else:
        return render_template("play.html")


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

