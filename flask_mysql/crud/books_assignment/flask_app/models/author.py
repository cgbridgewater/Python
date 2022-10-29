from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book



### AUTHOR CLASS (WORKING)
class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.book_id = data['LOOK HERE']
        self.books = []





### CREATE AND SAVE NEW AUTHOR (WORKING)
    @classmethod
    def createAuthor(cls,data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        print('CREATING AUTHOR')
        return connectToMySQL('books_schema').query_db(query,data)


### GET ALL USERS (WORKING)
    @classmethod
    def getAllAuthors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        pprint(results)
        authors = []
        for a in results:
            authors.append(cls(a))
        pprint("GETTING ALL AUTHORS")
        return authors





### (TESTING) Returns a good result i think??? (doesnt crash page but havent passed data yet)
    @classmethod
    def getAuthorsAndBooks(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT Join books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)
        pprint(results)  ### use this printstatement with nothing after!!!!    match id tags in print to match below needs!!!
        one_author = cls( results[0] )
        for one_book in results:
            # parse the book data to make instances of books and add them to the list
            book_data = { 
                "id" : one_book["books.id"],
                "title" : one_book["title"],
                "num_of_pages" : one_book["num_of_pages"],
                "created_at" : one_book["books.created_at"],
                "updated_at" : one_book["books.updated_at"],
                "author_id" : one_book["author_id"]
            }

            one_author.books.append( book.Book( book_data))
        return one_author



    @classmethod
    def getTheBooks(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        print(results)
        books = []
        for b in results:
            books.append(cls(b))
        return books









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