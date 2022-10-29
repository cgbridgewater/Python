from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo


### NINJA CLASS
class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']    
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        # self.owner = None


# ### CREATE AND SAVE NEW NINJA(WORKING)
    @classmethod
    def addNinja(cls,data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);"
        print("ADDING NINJA!")
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)


### READ NINJA DATA BY ID
    @classmethod
    def getOneNinja(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        if len(result) == 0: #if no users found, return an empty list
            return None
        else: # if at least one user found
            return cls(result[0])


### UPDATE NINJA (TESTING)
    @classmethod
    def updateNinja(cls,data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;"
        print("UPDATING NINJA")
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)


### DELETE USER BY ID (WORKING)
    @classmethod
    def deleteNinja(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        print("DELETING NINJA!")
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)