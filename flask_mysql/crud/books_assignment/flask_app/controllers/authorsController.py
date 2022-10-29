from pprint import pprint
from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app.models.favorite import Favorite



### WORKING
@app.route('/')
def index():
    return redirect('/authors')

### WORKING
@app.route('/authors')
def homeAuthors():
    return render_template("authors.html", authors = Author.getAllAuthors())


###  WORKING
@app.route("/authors/create" , methods=['POST'])
def createAuthor():
    Author.createAuthor(request.form)
    return redirect(f'/authors')


### ROUTE TO VIEW AUTHOR PAGE BY "ID" (WORKING)
@app.route('/authors/<int:id>')
def showAuthor(id):
    data = {
    "id" : id
    }
    return render_template("authors(one).html",  one_author = Author.getAuthorsAndBooks(data), one_book = Book.getAllBooks())


### ROUTE TO ADD FAVORITES BOOK/AUTHOR RELATION (WORKING)
@app.route("/authors/favorites", methods = ['POST'])
def addAuthorsFavorites():
    # data ={   ###########  only need this if manipulating request form names
    #     "book_id": request.form["book_id"],
    #     "author_id": request.form["author_id"],
    #     # "id" : request.form["author_id"]
    #     }
    author_id = request.form["author_id"]
    Favorite.createFavorites(request.form)
    pprint(request.form)
    return redirect(f'/authors/{author_id}')


