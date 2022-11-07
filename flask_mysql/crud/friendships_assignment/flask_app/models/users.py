from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint


### USER CLASS
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name'] 
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.friendships = []


### GET ALL USERS (WORKING)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        return connectToMySQL('friendship_schema').query_db(query)


### CREATE AND SAVE NEW USER (WORKING)
    @classmethod
    def saveUser(cls,data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        return connectToMySQL('friendship_schema').query_db(query,data)


### CREATE AND SAVE NEW FRIENDSHIP (WORKING)
    @classmethod
    def saveFriendship(cls,data):
        query = "INSERT INTO friendships (user_id, friend_id) VALUES (%(user_id)s, %(friend_id)s);"
        return connectToMySQL('friendship_schema').query_db(query,data)




### GET USER AND FRIENDS (testing)
    @classmethod
    def getFriends(cls):
        query = "SELECT f.first_name as friend_first , f.last_name as friend_last , u.first_name as user_first , u.last_name as user_last FROM users u LEFT JOIN friendships fs ON u.id = fs.user_id LEFT JOIN users f ON f.id = fs.friend_id;"
        result = connectToMySQL('friendship_schema').query_db(query) 
        pprint(result)
        return result 


### GET USER BY ID (testing)
    @classmethod
    def get_one_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('friendship_schema').query_db(query,data)
        if len(result) == 0: #if no users found, return an empty list
            return None
        else: # if at least one user found
            return cls(result[0])


### UPDATE USER BY ID (testing)
    @classmethod
    def updateUser(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s WHERE id = %(id)s;"
        return connectToMySQL('friendship_schema').query_db(query,data)



### DELETE USER BY ID (WORKING)
    @classmethod
    def deleteUser(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('friendship_schema').query_db(query,data) 