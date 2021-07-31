
from . import animals_app # importing our app obj from our app pkg
from flask_pymongo import PyMongo # importing PyMongo() obj for interfacing with our MongoDB database

animals_db = PyMongo(animals_app) # instantiating our DB obj for use with our app