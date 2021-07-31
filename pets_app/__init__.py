
# basically just initialize our app and DB here

from flask import Flask, render_template # importing Flask obj to make app and 'render_template' module to render HTML templates
from flask_pymongo import PyMongo # importing PyMongo() obj for interfacing with our MongoDB database
from dotenv import load_dotenv # importing 'load_dotenv()' to load our env variables
import os # importing Python library for interfacing with OS
load_dotenv()

pets_app = Flask(__name__) # initializing our app obj
pets_app.config["MONGO_URI"] = os.getenv("MONGO_URI") # configuring our DB location
animals_db = PyMongo(pets_app) # instantiating our DB obj for use with our app

@pets_app.route('/')
@pets_app.route('/index')
def index():
    return render_template('index.html')

# 'create' part of 'CRUD'
@pets_app.route('/create', methods=['POST', 'GET'])
def create():
    pass
