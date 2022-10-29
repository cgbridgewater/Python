from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author



### Book CLASS
class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']    
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.author_id = data['author_id']
        self.authors = []




### CREATE AND SAVE NEW BOOK (Testing)
    @classmethod
    def createBook(cls,data):
        query = "INSERT INTO books (title , num_of_pages, created_at, updated_at) VALUES (%(title)s , %(num_of_pages)s, NOW() , NOW());"
        print('CREATING BOOKS')
        return connectToMySQL('books_schema').query_db(query,data)


### GET ALL Book (Testing)
    @classmethod
    def getAllBooks(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        print("GETTING ALL BOOKS!!")
        pprint(results)
        books = []
        for b in results:
            books.append(cls(b))
        return books





### (TESTING) 
    @classmethod
    def getBooksWithAuthors(cls,data):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT Join authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)
        pprint(results)  ### use this printstatement with nothing after!!!!    match id tags in print to match below needs!!!
        one_book = cls( results[0] )
        for row in results:
            # parse the row data to make instances of the rows and add them to the list
            author_data = { 
                "id" : row["authors.id"],
                "name" : row["name"],
                "created_at" : row["authors.created_at"],
                "updated_at" : row["authors.updated_at"],
            }
            one_book.authors.append(author.Author(author_data))
        return one_book


    @classmethod
    def booksJoin(cls):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id;"
        pprint('JOINING BOOKS AND FAVS')
        pprint(query)
        return connectToMySQL('books_schema').query_db(query)
























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