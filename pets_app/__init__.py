
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

@pets_app.route('/')
@pets_app.route('/index')
def index():
    return render_template('index.html')

# 'create' part of 'CRUD'
@pets_app.route('/add_pet', methods=['POST', 'GET'])
def add_pet():
    add_pet_form = AddPet(request.form) # assign values of form's KV pairs (from request data) to 'add_pet_form' keys
    if request.method == 'POST' and add_pet_form.validate_on_submit():
        # if data is valid and is being POSTed, insert it into DB
        new_pet = {
            # Python dictionary/JS object/MongoDB record, populated with form data
            "name": add_pet_form.name.data,
            "species": add_pet_form.species.data,
            "age": add_pet_form.age.data,
            "sex": add_pet_form.sex.data,
            "description": add_pet_form.description.data
        }
        pets_db.db.pets.insert(new_pet) # insert new record into DB
        flash('Pet added successfully!') # success feedback msg
        return redirect(url_for('index')) # redirect to home page
    return render_template('add_pet.html', add_pet_form=add_pet_form)

# 'read' part of 'CRUD'
@pets_app.route('/read_pet/')
def read_pet():
    pass
