from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja


### DOJO CLASS
class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


### CREATE AND SAVE NEW Dojo (Testing...)
    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)


### GET ALL USERS (Testing)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for i in results:
            dojos.append(cls(i))
        return dojos


### (testing!!!!)
    @classmethod
    def getDojoAndNinjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print("LOOK HERE")
        print("LOOK HERE")
        print(results)  ### use this printstatement with nothing after!!!!    match id tags in print to match below needs!!!
        one_dojo = cls( results[0] )
        for one_ninja in results:
            # parse the ninja data to make instances of ninjas and add them to the list
            data = { 
                "id" : one_ninja["ninjas.id"],
                "first_name" : one_ninja["first_name"],
                "last_name" : one_ninja["last_name"],
                "age" : one_ninja["age"],
                "created_at" : one_ninja["ninjas.created_at"],
                "updated_at" : one_ninja["ninjas.updated_at"],
            }
            ninja_data = ninja.Ninja(data)
            one_dojo.ninjas.append(ninja_data)
        return one_dojo




# ### (testing!!!!)
#     @classmethod
#     def getDojoAndNinjas(cls,data):
#         query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
#         results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
#         # results will be a list of ninja info attached in the row
#         if len(results) == 0: #if no users found, return an empty list
#             return None
#         else: # if at least one user found
#             dojo = cls( results[0] )
#         for row_from_db in results:
#             # parse the ninja data to make instances of ninjas and add them to the list
#             ninja_data = {
#                 "id" : row_from_db["ninjas.id"],
#                 "first_name" : row_from_db["first_name"],
#                 "last_name" : row_from_db["last_name"],
#                 "age" : row_from_db["age"],
#                 "created_at" : row_from_db["created_at"],
#                 "updated_at" : row_from_db["updated_at"],
#             }
#             dojo.ninjas.append( ninja.Ninja( ninja_data ) )
#         return dojo













### GET USER BY ID (WORKING)
    @classmethod
    def get_one_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        if len(result) == 0: #if no users found, return an empty list
            return None
        else: # if at least one user found
            return cls(result[0])



# ### GET ALL USERS (WORKING)
#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM users;"
#         results = connectToMySQL('users_cr').query_db(query)
#         users = []
#         for i in results:
#             users.append(cls(i))
#         return users




# ### CREATE AND SAVE NEW USER (WORKING)
#     @classmethod
#     def save(cls,data):
#         query = "INSERT INTO users (first_name, last_name,email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
#         return connectToMySQL('users_cr').query_db(query,data)




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