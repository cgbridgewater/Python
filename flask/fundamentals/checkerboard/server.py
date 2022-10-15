from flask import Flask, render_template, request  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"




### MAIN PAGE ROUTE
# @app.route('/')
# def home_page():
#     return render_template("index.html")


# @app.route('/4')
# def eightby4():
#     return render_template("index_4.html")




###PLAY PAGE ROUTES WITH STACKED INPUT OPTIONS
@app.route('/')
@app.route('/<int:num>/', endpoint='<int:num>')
@app.route('/<int:num>/<int:nums>/', endpoint='/<int:num>/<int:nums>/')
def play(num= 8, nums = 8): 

### LOOP PRODUCES DIVS THAT THE BOXES ARE CREATED FROM
    # even= ''
    # odd = ''
    # output1 = ''
    # output2 = ''
    # for i in range(0,num):
    #     if i %2 == 0:
    #         output1 += f" {even} "
    #     else:
    #         output2 += f" {odd} "

    height = ' '
    output1 = ''
    for i in range(0,num):
        output1 += f" {height} "

    width = ' '
    output2 = ''
    for x in range(0,nums):
        output2 += f" {width} "

### IF STATEMENTS TO RETURN THE ROUTE REPLY
    # if request.endpoint == '/4':
    #     return render_template("index_4.html")
    
    if request.endpoint == '<int:num>':
        return render_template("index_4.html", num = num )
    
    if request.endpoint == '/<int:num>/<int:nums>/':
        return render_template("index_4.html", num = num, nums = nums )    
    
    else:
        return render_template("index_4.html")






### DINO GAME
@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("dinosaur.html")


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

