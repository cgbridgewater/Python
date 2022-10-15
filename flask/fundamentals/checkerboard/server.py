from flask import Flask, render_template, request  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


### INDEX ROUTES WITH STACKED INPUT OPTIONS - MAKES CHECKERS PAGE
@app.route('/')
@app.route('/<int:num>/', endpoint='<int:num>')
@app.route('/<int:num>/<int:nums>/', endpoint='/<int:nums>/')
@app.route('/<int:num>/<int:nums>/<string:color>/', endpoint='<string:color>/')
@app.route('/<int:num>/<int:nums>/<string:color>/<string:other_color>/', endpoint='<string:other_color>/')
def play(num= 8, nums = 8, color = None, other_color = None): 


    if request.endpoint == '<int:num>':
        return render_template("index.html", num = num )
    
    if request.endpoint == '/<int:nums>/':
        return render_template("index.html", num = num, nums = nums )    
    
    if request.endpoint == '<string:color>/':
        return render_template("index.html", num = num, nums = nums, color = color )    
    
    if request.endpoint == '<string:other_color>/':
        return render_template("index.html", num = num, nums = nums,color = color, other_color = other_color )    
    
    else:
        return render_template("index.html",  num = num )


### DINO GAME
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("dinosaur.html")


### Ensure this file is being run directly and not from a different module
### Run the app in debug mode.
if __name__=="__main__":
    app.run(debug=True)

