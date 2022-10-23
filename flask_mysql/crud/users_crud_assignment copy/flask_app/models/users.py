from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']    
        self.created_at = data['created_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_cr').query_db(query)
        users = []
        for i in results:
            users.append(cls(i))
        return users

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name,email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL('users_cr').query_db(query,data)
        return result

    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE users (name,weight) SET (%(name)s, %(weight)s);"
    #     result = connectToMySQL('user_cr').query_db(query,data)
    #     return result


### make delete
    #     @classmethod
    # def save(cls,data):
    #     query = "DELETE FROM users (name,weight) WHERE (%(name)s, %(weight)s);"
    #     result = connectToMySQL('user_cr').query_db(query,data)
    #     return result
    #     return result