from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
from flask_app.models import book


### CONSTRUCTOR
class Favorite:
    def __init__(self,data):
        self.book_id = data['book_id']
        self.author_id = data['author_id']



    @classmethod
    def readFavorites(cls):
        query = "SELECT * FROM favorites;"
        print('FETCHING Favorites')
        return connectToMySQL('books_schema').query_db(query,data)


### INSERT TO FAVORITES LIST (TESTING)
    @classmethod
    def createFavorites(cls,data):
        query = "INSERT INTO favorites (author_id , book_id) VALUES (%(author_id)s, %(book_id)s);"
        print('CREATING Favorites')
        return connectToMySQL('books_schema').query_db(query,data)


### GET ALL USERS (WORKING)
    @classmethod
    def getAuthorFavorites(cls, data):
        query = "SELECT * FROM favorites WHERE author_id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)
        pprint(results)
        favorites = []
        for a in results:
            favorites.append(cls(a))
        return favorites

    # @classmethod
    # def getBookFavorites(cls, data):
    #     query = "SELECT * FROM favorites WHERE author_id = (book_id) = (%(book_id)s) ;"
    #     results = connectToMySQL('books_schema').query_db(query)
    #     authors = []
    #     for a in results:
    #         authors.append(cls(a))
    #     return authors






    #     ### (TESTING)
    # @classmethod
    # def getAuthorsAndBooks(cls,data):
    #     query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = author.id LEFT Join books ON favorites.book_id = book.id WHERE authors.id = %(id)s;"
    #     # query = "SELECT * FROM authors LEFT JOIN books ON books.author_id = authors.id WHERE authors.id = %(id)s;"
    #     results = connectToMySQL('books_schema').query_db(query,data)
    #     print(results)  ### use this printstatement with nothing after!!!!    match id tags in print to match below needs!!!
    #     # one_dojo = cls( results[0] )
    #     # for one_ninja in results:
    #     #     # parse the ninja data to make instances of ninjas and add them to the list
    #     #     data = { 
    #     #         "id" : one_ninja["ninjas.id"],
    #     #         "first_name" : one_ninja["first_name"],
    #     #         "last_name" : one_ninja["last_name"],
    #     #         "age" : one_ninja["age"],
    #     #         "created_at" : one_ninja["ninjas.created_at"],
    #     #         "updated_at" : one_ninja["ninjas.updated_at"],
    #     #     }
    #     #     ninja_data = ninja.Ninja(data)
    #     #     one_dojo.ninjas.append(ninja_data)
    #     # return one_dojo