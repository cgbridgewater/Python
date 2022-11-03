from sre_parse import SPECIAL_CHARS
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt    
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


### USER CLASS
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']    
        self.password = data['password']    
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


### REGISTRATION VALIDATIONS
    @staticmethod
    def validate_registration(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 3: ### first name length check
            flash("First Name must be at least 3 characters.", "register")
            is_valid = False
        if len(user['last_name']) < 3: ### last name length check
            flash("Last Name must be at least 3 characters.", "register")
            is_valid = False
        if len(user['email']) < 3:    ### email length check
            flash("Email must be a valid email.", "register")
            is_valid = False
        if len(user['password']) < 3: ### password length check
            flash("Password must be a valid password.", "register")
            is_valid = False
        if len(user['confirm_password']) < 4: ### password length check
            flash("Password must be a valid password.", "register")
            is_valid = False
        if user['password'] != user['confirm_password']: #### passwords must match
            flash("Passwords must match!!", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):  ### checks email formating
            flash("Invalid email address!", "register")
            is_valid = False
        if User.email_exists(user):  ### check user email is origional
            flash("This email is already taken!", "register")
            is_valid = False 
        return is_valid ### if you make it this far, is good to go!


### LOGIN VALIDATIONS
    @staticmethod
    def validate_login(user):
        is_valid = True # we assume this is true
        if len(user['email']) < 3:    ### email length check
            flash("Email must be a valid email.", "login")
            is_valid = False
        if len(user['password']) < 3: ### password length check
            flash("Password must be a valid password.", "login")
            is_valid = False
        return is_valid ### if you make it this far, is good to go!


### CHECK FOR EXISTING EMAIL (WORKING)
    @classmethod 
    def email_exists(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('login_registration_schema').query_db(query,data) 
        if len(result) < 0: #if no users found, return an empty list
            return None
        else: # if at least one user found
            return cls(result[0])


### LOOK UP USER BY EMAIL
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("login_registration_scema").query_db(query,data)
        #didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])


### CREATE AND SAVE NEW USER (testing)
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s );"
        return connectToMySQL('login_registration_schema').query_db(query,data)


### GET USER BY ID (WORKING)
    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('login_registration_schema').query_db(query,data)
        if len(result) == 0: #if no users found, return an empty list
            return None
        else: # if at least one user found
            return cls(result[0])


### DELETE USER BY ID (WORKING)
    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('login_registration_schema').query_db(query,data) 




### UPDATE USER BY ID (WORKING)
    @classmethod
    def updateUser(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL('login_registration_schema').query_db(query,data)






#### check all below and save this just in case all users needed!!

# ### GET ALL USERS (testing)
#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM users;"
#         results = connectToMySQL('login_registartion_schema').query_db(query)
#         users = []
#         for i in results:
#             users.append(cls(i))
#         return users









