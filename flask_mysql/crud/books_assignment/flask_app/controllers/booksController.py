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


### ROUTE TO VIEW BOOK PAGE BY "ID" (WORKING)
@app.route('/books/<int:id>')
def showBooksFavorites(id):
    data = {
    "id" : id
    }
    return render_template("books(one).html", one_author = Author.getAllAuthors(), one_book = Book.getBooksWithAuthors(data))


# #####testing
@app.route("/books/favorites", methods = ['POST'])
def addBooksFavorites():
    # data ={   ###########  only need this if manipulating request form names
    #     "book_id": request.form["book_id"],
    #     "author_id": request.form["author_id"],
    #     # "id" : request.form["author_id"]
    #     }
    book_id = request.form["author_id"]
    Favorite.createFavorites(request.form)
    pprint(request.form)
    return redirect(f'/books/{book_id}')











#######  EXAMPLE ROUTES

# ### ROUTE TO CREATE NEW USER AND DIRECT TO USER PROFILE PAGE BY "ID" -- FORM AND SUBMISSION REQUIRED!!! (WORKING)
# @app.route("/users/creating" , methods=['POST'])
# def addUser():
#     new_user_id = User.save(request.form)
#     return redirect(f'/users/read/{new_user_id}')



#     ### ROUTE TO VIEW USER PROFILE PAGE BY "ID" (WORKING)
# @app.route('/users/read/<int:id>')
# def showOneUser(id):
#     data = {
#     "id" : id
#     }
#     return render_template("read(one).html", user = User.get_one_user(data))


#     ### ROUTE TO EDIT USER PROFILE BY "ID" (WORKING)
# @app.route('/users/edit/<int:id>')
# def editUser(id):
#     data = {
#     "id" : id
#     }
#     return render_template("edit.html", user = User.get_one_user(data))



# ### ROUTE TO UPDATE USER PROFILE AND REDIRECT TO USER PROFILE PAGE BY "ID" -- FORM AND SUBMISSION REQUIRED!!! (WORKING)
# @app.route('/users/updating/<int:id>', methods =['POST'])
# def updateUser(id):
#     data = {
#         "first_name": request.form["first_name"],
#         "last_name": request.form["last_name"],
#         "email": request.form["email"],
#         "id" : id
#         }
#     print('HELLO!!!!')
#     User.updateUser(data)
#     return redirect(f'/users/read/{id}') 


    
# ### ROUTE TO DELETE USER BY "ID" -- DRIVEN BY A BUTTON SUBMISSION OR SOMETHING (WORKING)
# @app.route('/users/delete/<int:id>')
# def deleteUser(id):
#     data = {
#     "id" : id
#     }
#     User.deleteUser(data)
#     return redirect('/users') 




# ### DINO GAME CATCH ALL (WORKING)
# @app.route('/', defaults = {'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return render_template("dinosaur.html")
