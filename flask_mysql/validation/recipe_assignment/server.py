from flask_app import app
from flask_app.controllers import recipesController, usersController, uiController



if __name__ == "__main__":
    app.run(debug=True)

