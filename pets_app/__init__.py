
# basically just initialize our app and DB here

from flask import Flask, render_template, request, redirect, url_for, flash # importing Flask obj to make app 
# also importing 'render_template' module to render HTML templates
# also importing 'request' module to get client request data that's going from client to server
# also importing 'redirect' and 'url_for' to redirect to specific routes/URLs
# also importing 'flash' to display feedback msgs

from flask_pymongo import PyMongo # importing PyMongo() obj for interfacing with our MongoDB database
from dotenv import load_dotenv # importing 'load_dotenv()' to load our env variables
import os # importing Python library for interfacing with OS
load_dotenv()

pets_app = Flask(__name__) # initializing our app obj
pets_app.config["MONGO_URI"] = os.getenv("MONGO_URI") # configuring our DB location
pets_app.config["SECRET_KEY"] = os.getenv("SECRET_KEY") # configuring our secret key to use web forms

from .database import pets_db # importing our initialized DB object
from .forms import AddPet # importing our 'AddPet' form class

from pets_app.crud_pets import crud_pets # importing our Blueprint of pets-related CRUD routes

pets_app.register_blueprint(crud_pets) # registering our pets-related CRUD Blueprint

@pets_app.route('/')
@pets_app.route('/index')
def index():
    return render_template('index.html')
