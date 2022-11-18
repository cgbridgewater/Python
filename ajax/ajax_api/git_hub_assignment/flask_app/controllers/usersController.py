from flask_app import app
from flask_app.models.user import User
from flask import request, jsonify


@app.route('/user/create', methods = ['POST'])
def f_create_user():
    print(request.form)
    if User.validate_new_user_form(request.form):
        User.add_user(request.form)
        return jsonify(status = 200, message = 'All good here! The user was added!')

    return jsonify(status = 501, message = 'One or both fields were empty')

@app.route('/user/get_all')
def get_users():
    users = User.get_all_users()
    return jsonify(all_users = users)
    
