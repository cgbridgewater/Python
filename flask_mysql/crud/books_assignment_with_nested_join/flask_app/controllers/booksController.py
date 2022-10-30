from pprint import pprint
from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app.models.favorite import Favorite


###WORKING
@app.route('/books')
def homeBooks():
    return render_template("books.html", books = Book.getAllBooks())


### ROUTE TO CREATE NEW BOOK AND DIRECT TO BOOKS ADD FORM (WORKING)
@app.route("/books/create" , methods=['POST'])
def createBook():
    Book.createBook(request.form)
    return redirect(f'/books')


# ### ROUTE TO VIEW BOOK PAGE BY "ID" (WORKING)   DROP DOWN USES ALL OPTIONS
# @app.route('/books/<int:id>')
# def showBooksFavorites(id):
#     data = {
#     "id" : id
#     }
#     return render_template("books(one).html", one_author = Author.getAllAuthors(), one_book = Book.getBooksWithAuthors(data))





### ROUTE TO VIEW BOOK PAGE BY "ID" -- NESTED JOIN MAKES DROP DOWN ONLY USE UNUSED OPTIONS!!!!
@app.route('/books/<int:id>')
def showNonFavoriteBooks(id):
    data = {
    "id" : id
    }
    return render_template("books(one).html", one_author = Author.getNotFavoritesAuthors(data), one_book = Book.getBooksWithAuthors(data))


















###  (WORKING)
@app.route("/books/favorites", methods = ['POST'])
def addBooksFavorites():
    # data ={   ###########  only need this if manipulating request form names
    #     "book_id": request.form["book_id"],
    #     "author_id": request.form["author_id"],
    #     # "id" : request.form["author_id"]
    #     }
    book_id = request.form["book_id"]
    Favorite.createFavorites(request.form)
    pprint(request.form)
    return redirect(f'/books/{book_id}')

