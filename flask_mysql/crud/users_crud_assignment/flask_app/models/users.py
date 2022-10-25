from flask_app.config.mysqlconnection import connectToMySQL

### USER CLASS
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']    
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


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
        result = connectToMySQL('users_cr').query_db(query,data)
        return result


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
        result = connectToMySQL('users_cr').query_db(query,data)
        return result


### DELETE USER BY ID (WORKING)
    @classmethod
    def deleteUser(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_cr').query_db(query,data) 