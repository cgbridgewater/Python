from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import users
import datetime


### Ride CLASS
class Ride:
    def __init__(self,data):
        self.id = data['id']
        self.rider_id = data['rider_id']
        self.driver_id = data['driver_id']
        self.destination = data['destination']
        self.pick_up = data['pick_up']
        self.date = data['date']
        self.details = data['details']
        self.comments = data['comments']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.rider = None
        self.driver = None
        self.rides = []


#### validations
    @staticmethod
    def validate_form(ride):
        is_valid = True # we assume this is true
        try:
            datetime.datetime.strptime(ride['date'], '%Y-%m-%d')
        except ValueError:
            flash("A Pick up date must be provided." , "ride")
            is_valid = False    # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        if len(ride['destination']) < 3: ### Cookie Type length check
            flash("A destination must be at least 2 characters." , "ride")
            is_valid = False
        if len(ride['pick_up']) < 3:    ### Quantity length check (form catches zero and negative numbers)
            flash("A pick up location must be at least 2 characters." , "ride")
            is_valid = False
        if len(ride['details']) < 10: ### Customer Name length check
            flash("Details must be provided" , "ride")
            is_valid = False
        return is_valid ### if you make it this far, is good to go!


    ### UPDATE VALIDATION
    @staticmethod
    def validate_update(ride):
        is_valid = True # we assume this is true
        if len(ride['pick_up']) < 3:    ### Quantity length check (form catches zero and negative numbers)
            flash("A pick up location must be at least 2 characters." , "ride")
            is_valid = False
        if len(ride['details']) < 10: ### Customer Name length check
            flash("Details must be provided" , "ride")
            is_valid = False
        return is_valid ### if you make it this far, is good to go!


### CREATE AND SAVE NEW USER (WORKING)
    @classmethod
    def save_ride(cls,data):
        query = '''
        INSERT INTO rides (rider_id, destination, pick_up, details, date) VALUES (%(rider_id)s, %(destination)s, %(pick_up)s, %(details)s , %(date)s );
        '''
        return connectToMySQL('ohana_schema').query_db(query,data)


### READ RIDE BY ID (WORKING)
    @classmethod
    def get_ride_by_id(cls,data):
        query = '''
        SELECT * FROM rides WHERE id = %(id)s;
        '''
        result = connectToMySQL('ohana_schema').query_db(query,data)
        print('AAA')
        print(result)
        if len(result) == 0: #if no users found, return an empty list
            return None
        else: # if at least one user found
            return cls(result[0])


### UPDATE RIDE BY ID (WORKING)
    @classmethod
    def update_ride(cls,data):
        query = "UPDATE rides SET pick_up = %(pick_up)s, details = %(details)s WHERE id = %(id)s;"
        return connectToMySQL('ohana_schema').query_db(query,data)


### DELETE RIDE BY ID (WORKING)
    @classmethod
    def delete_ride(cls,data):
        query = "DELETE FROM rides WHERE id = %(id)s;"
        result= connectToMySQL('ohana_schema').query_db(query,data) 
        return  result


### UPDATE RIDE BY ID (WORKING)
    @classmethod
    def accept_ride(cls,data):
        query = "UPDATE rides SET driver_id = %(driver_id)s WHERE rides.id = %(id)s;"
        return connectToMySQL('ohana_schema').query_db(query,data)


### UPDATE RIDE BY ID (WORKING)
    @classmethod
    def cancel_ride(cls,data):
        query = "UPDATE rides SET driver_id = NULL WHERE rides.id = %(id)s;"
        pprint(query)
        pprint("AAAAAAAAA")
        return connectToMySQL('ohana_schema').query_db(query,data)

    ### GET EVERYTHING
    @classmethod
    def get_all_users_and_rides(cls):
        query = '''
        SELECT * FROM rides 
        LEFT JOIN users AS rider ON rider.id = rides.rider_id 
        LEFT JOIN users AS driver ON driver.id = rides.driver_id;
        '''
        results = connectToMySQL('ohana_schema').query_db(query)
        all_rides = []
        print("A")
        for row in results:# Create a Tweet class instance from the information from each db row
            for key in row:
                print(key,"\t\t",row[key])
            one_ride = cls(row)# Prepare to make a User class instance, looking at the class in models/user.py
            ### rider
            rider_data = { # Any fields that are used in BOTH tables will have their name changed, which depends on the order you put them in the JOIN query, use a print statement in your classmethod to show this.
                "id": row['id'], 
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
            }
            ### driver
            driver_data = { # Any fields that are used in BOTH tables will have their name changed, which depends on the order you put them in the JOIN query, use a print statement in your classmethod to show this.
                    "id": row['driver.id'], 
                    "first_name": row['driver.first_name'],
                    "last_name": row['driver.last_name'],
                    "email": row['driver.email'],
                    "password": row['driver.password'],
                    "created_at": row['driver.created_at'],
                    "updated_at": row['driver.updated_at'],
            }
            ### rider
            rider = users.User(rider_data)
            one_ride.rider = rider       
            ### driver
            driver = users.User(driver_data)
            one_ride.driver = driver 
            all_rides.append(one_ride) 
        return all_rides
