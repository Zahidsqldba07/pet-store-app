
# all CRUD-related routes about pets will go here

from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint # importing Flask obj to make app 
# also importing 'render_template' module to render HTML templates
# also importing 'request' module to get client request data that's going from client to server
# also importing 'redirect' and 'url_for' to redirect to specific routes/URLs
# also importing 'flash' to display feedback msgs
# also importing 'Blueprint' for grouping related routes together

crud_pets = Blueprint('crud_pets', __name__) # our Blueprint for all pet-related CRUD routes

from .database import pets_db # importing our initialized DB object
from .forms import AddPet # importing our 'AddPet' form class

# 'create' part of 'CRUD'
@crud_pets.route('/add_pet', methods=['POST', 'GET'])
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
        new_pet_name = add_pet_form.name.data
        pets_db.db.pets.insert(new_pet) # insert new record into DB
        flash('Pet added successfully!') # success feedback msg
        return redirect(url_for('crud_pets.read_pet', name=new_pet_name)) # redirect to pet's new 'read_pet' pg
    return render_template('add_pet.html', add_pet_form=add_pet_form)

# 'read' part of 'CRUD'
@crud_pets.route('/read_pet/<name>')
def read_pet(name):
    # find pet based on given pet's name, print pet's info if there's a match
    current_pet = pets_db.db.pets.find_one({"name": name}) # 'find_one()' should convert our PyMongo cursor obj of the record here to an iterable Python dictionary
    return render_template('read_pet.html', current_pet=current_pet) # passing our current Python dictionary/MongoDB record of the newly added pet to a template for rendering