from urllib import request
from flask import Flask, render_template, request  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html")  # Return index html as a response

@app.route('/success')
def success():
    return "Great Success!!" #returns string as a response


#### this one is the working command!!!!! ####

@app.route('/hello/<string:banana>/<int:num>')
def hello(banana=None,num=None): 
    return render_template("hello.html", banana=banana, num = num )    



####stacking!!####
# @app.route('/hello/') #endpoint='hello')
# @app.route('/hello/<string:banana>/', endpoint='<string:banana>')
# @app.route('/hello/<string:banana>/<int:num>', endpoint='<string:banana>/<int:num>')
# def hello(banana=None,num=None): 
#     if request.endpoint == '/hello':
#         return render_template("hello.html")    
#     if request.endpoint == '<string:banana>':
#         return render_template("hello.html", banana=banana )
#     if request.endpoint == '<string:banana>/<int:num>':
#         return render_template("hello.html", banana=banana, num = num )    
#     else:
#         return render_template("hello.html")



# @app.route('/hola/<string:banana>/<int:num>')
# def hola(banana, num):
#     return f"Hola {banana * num}"

# @app.route('/users/<username>/<id>')
# def show_user_profile(username,id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id


@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)








if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.