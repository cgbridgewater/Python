from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/user/*": {"origins": "*"}})
app.secret_key = "mums the word"
