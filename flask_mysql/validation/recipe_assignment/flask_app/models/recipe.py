from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import users
import datetime


### USER CLASS
class Recipe:
    def __init__(self,data):
        self.id = data['id']
        # self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']    
        self.date_made = data['date_made']    
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None
        self.recipes = []


#### validations
    @staticmethod
    def validate_recipe(order):
        is_valid = True # we assume this is true
        try:
            datetime.datetime.strptime(order['date_made'], '%Y-%m-%d')
        except ValueError:
            flash("A date must be provided." , "recipe")
            is_valid = False    # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        if len(order['name']) < 3: ### Customer Name length check
            flash("Name must be at least 2 characters." , "recipe")
            is_valid = False
        if len(order['description']) < 3: ### Cookie Type length check
            flash("Description must be at least 2 characters." , "recipe")
            is_valid = False
        if len(order['instruction']) < 3:    ### Quantity length check (form catches zero and negative numbers)
            flash("Instructions must be at least 2 characters." , "recipe")
            is_valid = False
        return is_valid ### if you make it this far, is good to go!


### CREATE AND SAVE NEW RECIPE (WORKING)
    @classmethod
    def save_recipe(cls,data):
        query = '''
        INSERT INTO recipes (user_id , name , description , instruction , date_made, under_30 ) 
        VALUES ( %(user_id)s, %(name)s , %(description)s , %(instruction)s , %(date_made)s , %(under_30)s );
        '''
        return connectToMySQL('recipe_schema').query_db(query,data)


### READ RECIPE BY ID (WORKING)
    @classmethod
    def get_one_recipe(cls,data):
        query = '''
        SELECT * FROM recipes WHERE id = %(id)s;
        '''
        result = connectToMySQL('recipe_schema').query_db(query,data)
        print(result)
        if len(result) == 0: #if no users found, return an empty list
            return None
        else: # if at least one user found
            return cls(result[0])


    ### READ RECIPE BY ID (WORKING)
    @classmethod
    def get_one_recipe_and_user(cls,data):
        query = '''
        SELECT recipes.id, recipes.created_at, recipes.updated_at, instruction, description, name, date_made, under_30,
        users.id as user_id, first_name, last_name, email,password, users.created_at as uc, users.updated_at as uu FROM recipes
        JOIN users ON recipes.user_id = users.id
        WHERE user_id = %(user_id)s AND recipes.id = %(id)s;
        '''
        results = connectToMySQL('recipe_schema').query_db(query,data)
        pprint(results)
        all_recipes = []
        for row in results:# Create a Tweet class instance from the information from each db row
            one_recipe = cls(row)# Prepare to make a User class instance, looking at the class in models/user.py
            one_recipe.creator = users.User( { # Any fields that are used in BOTH tables will have their name changed, which depends on the order you put them in the JOIN query, use a print statement in your classmethod to show this.
                "id": row['user_id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['uc'],
                "updated_at": row['uu'],
            })
            # author = recipe.Recipe(one_recipes_author_info)### Create the User class instance that's in the user.py model file
            # one_recipe.creator = author ### Associate the Tweet class instance with the User class instance by filling in the empty creator attribute in the Tweet class
            all_recipes.append(one_recipe) ### Append the Tweet containing the associated User to your list of tweets
        return all_recipes


    ### READ ALL RECIPES PLUS USER (WORKING)
    @classmethod
    def get_all_recipes(cls):# Get all recipes, and their one associated User that created it
        query = """
        SELECT recipes.id, recipes.created_at, recipes.updated_at, instruction, description, name, date_made, under_30,
        users.id as user_id, first_name, last_name, email,password, users.created_at as uc, users.updated_at as uu
        FROM recipes
        JOIN users on users.id = recipes.user_id;
        """
        results = connectToMySQL('recipe_schema').query_db(query)
        pprint(results)
        all_recipes = []
        for row in results:# Create a Tweet class instance from the information from each db row
            one_recipe = cls(row)# Prepare to make a User class instance, looking at the class in models/user.py
            one_recipe.creator = users.User( { # Any fields that are used in BOTH tables will have their name changed, which depends on the order you put them in the JOIN query, use a print statement in your classmethod to show this.
                "id": row['user_id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['uc'],
                "updated_at": row['uu'],
            })
            # author = recipe.Recipe(one_recipes_author_info)### Create the User class instance that's in the user.py model file
            # one_recipe.creator = author ### Associate the Tweet class instance with the User class instance by filling in the empty creator attribute in the Tweet class
            all_recipes.append(one_recipe) ### Append the Tweet containing the associated User to your list of tweets
        return all_recipes


### UPDATE USER BY ID (WORKING)
    @classmethod
    def update_recipe(cls,data):
        query = '''
        UPDATE recipes SET name = %(name)s , description = %(description)s , instruction = %(instruction)s , date_made = %(date_made)s , under_30 = %(under_30)s WHERE id = %(id)s;
        '''
        return connectToMySQL('recipe_schema').query_db(query,data)



    ### DELETE USER BY ID (WORKING)
    @classmethod
    def delete_recipe(cls,data):
        query = '''
        DELETE FROM recipes WHERE id = %(id)s;
        '''
        return connectToMySQL('recipe_schema').query_db(query,data) 