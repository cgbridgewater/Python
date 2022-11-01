from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

### USER CLASS
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']    
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


###Validations
    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 3: ### first name length check
            flash("First Name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3: ### last name length check
            flash("Last Name must be at least 3 characters.")
            is_valid = False
        if len(user['email']) < 3:    ### email length check
            flash("Email must be a valid email.")
            is_valid = False
        if len(user['password']) < 3: ### password length check
            flash("Email must be a valid email.")
            is_valid = False
        if len(user['confirm_password']) < 3: ### password length check
            flash("Email must be a valid email.")
            is_valid = False
        if user['password'] != user['confirm_password']: #### passwords must match
            flash("Passwords must match!!")
            is_valid = False
        if User.email_exists(user):  ### check user email is origional
            flash("This email is already taken!")
            is_valid = False 
        if not EMAIL_REGEX.match(user['email']):  ### checks email formating
            flash("Invalid email address!")
            is_valid = False
        return is_valid ### if you make it this far, is good to go!


### GET USER BY EMAIL (WORKING)
    @classmethod 
    def email_exists(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('users_cr').query_db(query,data) 
        print("A")
        print(result)
        if len(result) == 0: #if no users found, return an empty list
            return None
        else: # if at least one user found
            return cls(result[0])


### CREATE AND SAVE NEW USER (WORKING)
    @classmethod
    def logIn(cls,data):
        query = '''
        INSERT INTO users (first_name, last_name,email) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s);
        '''
        return connectToMySQL('users_cr').query_db(query,data)




### GET ALL USERS (WORKING)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_cr').query_db(query)
        users = []
        for i in results:
            users.append(cls(i))
        return users


### CREATE AND SAVE NEW USER (WORKING)
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name,email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL('users_cr').query_db(query,data)



### GET USER BY ID (WORKING)
    @classmethod
    def get_one_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('users_cr').query_db(query,data)
        if len(result) == 0: #if no users found, return an empty list
            return None
        else: # if at least one user found
            return cls(result[0])


### UPDATE USER BY ID (WORKING)
    @classmethod
    def updateUser(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL('users_cr').query_db(query,data)



### DELETE USER BY ID (WORKING)
    @classmethod
    def deleteUser(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_cr').query_db(query,data) 