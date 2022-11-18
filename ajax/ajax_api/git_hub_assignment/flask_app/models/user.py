from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_new_user_form(form_data):
        # No form fields to be empty
        is_valid = True

        if len(form_data['first_name']) == 0:
            is_valid = False
        if len(form_data['last_name']) == 0:
            is_valid = False
        
        return is_valid

    @classmethod
    def add_user(cls,data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"

        return connectToMySQL('api_db').query_db(query,data)

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"

        results = connectToMySQL('api_db').query_db(query)

        users = []

        for result in results:
            users.append({
                'first_name' : result['first_name'],
                'last_name' : result['last_name']
            })

        return users