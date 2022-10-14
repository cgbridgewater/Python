from flask import Flask, render_template, request
app = Flask(__name__)

###HOME PAGE
@app.route('/')          
def hello_world():
    return render_template('index.html')

###PLAY PAGE ROUTES WITH STACKED INPUT OPTIONS
@app.route('/play/', endpoint='play')
@app.route('/play/<int:num>/', endpoint='<int:num>')
@app.route('/play/<int:num>/<string:color>/', endpoint='<int:num>/<string:color>')
def play(num= 3,color=None): 

### LOOP PRODUCES DIVS THAT THE BOXES ARE CREATED FROM
    word= ''
    output = ''
    for i in range(0,num):
        output += f" {word} "
        # list.append(output)

### IF STATEMENTS TO RETURN THE ROUTE REPLY
    if request.endpoint == '/play':
        return render_template("play.html")   
    
    if request.endpoint == '<int:num>':
        return render_template("play.html", num = num )
    
    if request.endpoint == '<int:num>/<string:color>':
        return render_template("play.html", num = num, color = color )    
    
    else:
        return render_template("play.html")


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.