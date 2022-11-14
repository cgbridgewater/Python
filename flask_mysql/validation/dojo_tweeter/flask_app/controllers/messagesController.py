from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user import User
from flask_app.models.message import Message


### ROUTE FOR FRIENDS PAGE 
@app.route('/dashboard/friends')
def all_users():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("user_friends.html", messages = Message.get_user_messages(data),user = User.get_one(data)) ### This should be a joined list and all friends by id



@app.route('/post_message', methods =['POST'])
def post_message():
    if 'user_id' not in session:
        msg = "you must be logged in!"
        return redirect('/logout')
    data ={
        'sender_id': request.form['sender_id'],
        'receiver_id': request.form['receiver_id'],
        'content': request.form['content']
    }
    Message.save(data)
    return redirect('/dashboard')


@app.route('/delete_message/<int:id>')
def delete_message(id):
    data = {
        "id" : id
    }
    Message.delete(data)
    return redirect('/dashboard')