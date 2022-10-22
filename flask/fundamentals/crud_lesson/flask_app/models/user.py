from sqlite3 import connect
from flask.fundamentals.first_flask_mysql.mysqlconnection import MySQLConnection
import flask_app.config.mysqlDB connect
from pprint import pprint
mydb = 'first_flask'

class User:
    def __init__ (self, data):
        self.id = data['id']
        self.id = data['first_name']
        self.id = data['last_name']
        self.id = data['occupation']
        self.id = data['created_at']
        self.id = data['updated_at']

    @classmethod
    def getAll(cls):
        query = '''
        SELECT * 
        FROM friends;'''
        things = connect(mydb).query_db(query)
        pprint(things)
        output = []
        for stuff in things:
            output.append(cls(stuff))
        pprint(output)
        return output