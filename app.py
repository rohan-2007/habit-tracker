import os
from pymongo import MongoClient
from flask import Flask
from routes import pages
from dotenv import load_dotenv

import certifi
ca=certifi.where()

load_dotenv

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages)
    client = MongoClient(os.environ.get("MONGODB_URI"), tlsCAFile=ca)
    app.db = client.get_default_database()

    return app
