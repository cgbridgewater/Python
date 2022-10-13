from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo') 
def dojo(): 
    return 'Dojo!'  #returns Dojo!

@app.route('/say/<default>')
def say(default):
    return f"Hi {default}" #returns input


# @app.route('/repeat/<int:num>/<string:repeat>')
# def repeat(num, repeat):
#     return f"{num * repeat}"      #returns  int * string
@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

