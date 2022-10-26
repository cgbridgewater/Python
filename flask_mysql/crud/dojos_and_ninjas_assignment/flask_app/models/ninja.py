from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

#### CRUD EXAMPLES BELOW!!!! 





### NINJA CLASS
class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']    
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.owner = None



### CREATE AND SAVE NEW Ninja (WORKING)
    @classmethod
    def create(cls,data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)














# ### GET ALL USERS (WORKING)
#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM users;"
#         results = connectToMySQL('users_cr').query_db(query)
#         users = []
#         for i in results:
#             users.append(cls(i))
#         return users





# ### GET USER BY ID (WORKING)
#     @classmethod
#     def get_one_user(cls,data):
#         query = "SELECT * FROM users WHERE id = %(id)s;"
#         result = connectToMySQL('users_cr').query_db(query,data)
#         if len(result) == 0: #if no users found, return an empty list
#             return None
#         else: # if at least one user found
#             return cls(result[0])


# ### UPDATE USER BY ID (WORKING)
#     @classmethod
#     def updateUser(cls,data):
#         query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
#         return connectToMySQL('users_cr').query_db(query,data)



# ### DELETE USER BY ID (WORKING)
#     @classmethod
#     def deleteUser(cls,data):
#         query = "DELETE FROM users WHERE id = %(id)s;"
#         return connectToMySQL('users_cr').query_db(query,data) 