from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


### USER CLASS
class Order:
    def __init__(self,data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']    
        self.boxes = data['boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


###Validations (testing)
    @staticmethod
    def validateOrder(order):
        is_valid = True # we assume this is true
        if len(order['customer_name']) < 2: ### Customer Name length check
            flash("Name must be at least 2 characters.")
            print("name flash")
            is_valid = False
        if len(order['cookie_type']) < 2: ### Cookie Type length check
            flash("Cookie Type must be at least 2 characters.")
            print("type flash")
            is_valid = False
        if len(order['boxes']) < 1:    ### Quantity length check (form catches zero and negative numbers)
            flash("Quantity must be greater than zero.")
            print("QTY flash")
            is_valid = False
        return is_valid ### if you make it this far, is good to go!


### GET ALL ORDERS (WORKS)
    @classmethod
    def getAllOrders(cls):
        query = "SELECT * FROM cookie_orders;"
        results = connectToMySQL('cookies_schema').query_db(query)
        users = []
        for i in results:
            users.append(cls(i))
        return users


### CREATE AND SAVE NEW ORDER (WORKS)
    @classmethod
    def saveOrder(cls,data):
        query = "INSERT INTO cookie_orders (customer_name, cookie_type,boxes) VALUES (%(customer_name)s, %(cookie_type)s, %(boxes)s);"
        return connectToMySQL('cookies_schema').query_db(query,data)


### GET ORDER BY ID (WORKS)
    @classmethod
    def getByOrderId(cls,data):
        query = "SELECT * FROM cookie_orders WHERE id = %(id)s;"
        result = connectToMySQL('cookies_schema').query_db(query,data)
        if len(result) == 0: #if no users found, return an empty list
            return None
        else: # if at least one user found
            return cls(result[0])


### UPDATE ORDER BY ID (WORKS)
    @classmethod
    def updateOrder(cls,data):
        query = "UPDATE cookie_orders SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, boxes = %(boxes)s WHERE id = %(id)s;"
        return connectToMySQL('cookies_schema').query_db(query,data)


### DELETE ORDER BY ID (WORKS)
    @classmethod
    def deleteOrder(cls,data):
        query = "DELETE FROM cookie_orders WHERE id = %(id)s;"
        return connectToMySQL('cookies_schema').query_db(query,data) 