# from flask_app import app
# from flask import render_template, request, redirect
# from flask_app.models.dojo import Dojo 
# from flask_app.models.ninja import Ninja




# ### ROUTE TO REDIRECT TO DOJO HOME (WORKING)
# @app.route('/')
# def index():
#     return redirect("/dojos")


# ### ROUTE TO DOJO HOME and FETCHING DOJO DATA (WORKING)
# @app.route('/dojos')
# def home():
#     return render_template("index.html", dojos = Dojo.get_all())



# ### ROUTE TO CREATE NEW DOJO AND DIRECT TO DOJO HOME (WORKING)
# @app.route("/dojos/create" , methods=['POST'])
# def addUser():
#     Dojo.create(request.form)
#     return redirect('/dojos')



# ### ROUTE TO VIEW USER PROFILE PAGE BY "ID" (NOT WORKING)
# @app.route('/dojos/<int:id>')
# def showOneDojo(id):
#     data = {
#     "id" : id
#     }
#     return render_template("dojo(one).html", dojo = Dojo.getDojoAndNinjas(data))







# #######  EXAMPLE ROUTES






# #     ### ROUTE TO EDIT USER PROFILE BY "ID" (WORKING)
# # @app.route('/users/edit/<int:id>')
# # def editUser(id):
# #     data = {
# #     "id" : id
# #     }
# #     return render_template("edit.html", user = User.get_one_user(data))



# # ### ROUTE TO UPDATE USER PROFILE AND REDIRECT TO USER PROFILE PAGE BY "ID" -- FORM AND SUBMISSION REQUIRED!!! (WORKING)
# # @app.route('/users/updating/<int:id>', methods =['POST'])
# # def updateUser(id):
# #     data = {
# #         "first_name": request.form["first_name"],
# #         "last_name": request.form["last_name"],
# #         "email": request.form["email"],
# #         "id" : id
# #         }
# #     print('HELLO!!!!')
# #     User.updateUser(data)
# #     return redirect(f'/users/read/{id}') 


    
# # ### ROUTE TO DELETE USER BY "ID" -- DRIVEN BY A BUTTON SUBMISSION OR SOMETHING (WORKING)
# # @app.route('/users/delete/<int:id>')
# # def deleteUser(id):
# #     data = {
# #     "id" : id
# #     }
# #     User.deleteUser(data)
# #     return redirect('/users') 




# ### DINO GAME CATCH ALL (WORKING)
# @app.route('/', defaults = {'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return render_template("dinosaur.html")
