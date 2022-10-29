from flask_app import app
from flask_app.controllers import ninjasController, dojosController # ,ninja_and_dojosController

if __name__ == "__main__":
    app.run(debug=True)

