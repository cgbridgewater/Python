from pprint import pprint
from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author


### BOOK Constructor
class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']    
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.author_id = data['author_id']
        self.authors = []


### CREATE AND SAVE NEW BOOK (WORKING)
    @classmethod
    def createBook(cls,data):
        query = "INSERT INTO books (title , num_of_pages, created_at, updated_at) VALUES (%(title)s , %(num_of_pages)s, NOW() , NOW());"
        print('CREATING BOOKS')
        return connectToMySQL('books_schema').query_db(query,data)


### GET ALL Book (WORKING)
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


### (WORKING) 
    @classmethod
    def getBooksWithAuthors(cls,data):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT Join authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)
        pprint("GET BOOKS WITH AUTHORS")
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



### (WORKING)
    @classmethod
    def getNotFavoritesBooks(cls,data): 
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s);"
        results = connectToMySQL('books_schema').query_db(query,data)
        pprint("NOT FAVORITED BOOK LIST")
        pprint(results)
        nonFavBooks = []
        for b in results:
            nonFavBooks.append(cls(b))
        return nonFavBooks






# ### (WORKING but not in needed)
#     @classmethod
#     def booksJoin(cls):
#         query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id;"
#         pprint('JOINING BOOKS AND FAVS')
#         pprint(query)
#         return connectToMySQL('books_schema').query_db(query)
    #     return nonFavBooks