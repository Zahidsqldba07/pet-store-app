
# all CRUD-related routes about pets will go here

from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint # importing Flask obj to make app 
# also importing 'render_template' module to render HTML templates
# also importing 'request' module to get client request data that's going from client to server
# also importing 'redirect' and 'url_for' to redirect to specific routes/URLs
# also importing 'flash' to display feedback msgs
# also importing 'Blueprint' for grouping related routes together

crud_pets = Blueprint('crud_pets', __name__) # our Blueprint for all pet-related CRUD routes

from .database import pets_db # importing our initialized DB object
from .forms import AddPet, NewAge, NewDescription, NewGender, NewSpecies, NewName # importing our 'AddPet' form class
# and also our 'update' form classes

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
    return render_template('read_pet.html', current_pet=current_pet, name=name) # passing our current Python dictionary/MongoDB record of the newly added pet to a template for rendering, doing same with current pet's name

''' 'update' part of 'CRUD' '''

@crud_pets.route('/update_pet/<name>')
def update_pet(name):
    # list of links to 'update pet info' forms for the given pet
    return render_template('update_pet.html', name=name)

@crud_pets.route('/update_name/<name>', methods=['POST', 'GET'])
def update_name(name):
    # find pet based on given pet's name, update pet's name if there's a match
    current_pet = pets_db.db.pets.find_one({"name": name}) # 'find_one()' should convert our PyMongo cursor obj of the record here to an iterable Python dictionary
    name_form = NewName(request.form) # get form data KV pairs, assign them to new NewName form object
    if request.method == 'POST':
        # if we're POSTing valid data, let's update the current pet's name 
        current_pet['name'] = name_form.new_name.data
        flash('Pet\'s name updated successfully!') # success feedback msg
        return redirect(url_for('index')) # return to home page
    else:
        # if we're not POSTing anything, let's return the regular 'update_name' page
        return render_template('update_name.html', name=name, name_form=name_form) # our template with 'update name' form and 'name' variable for current name passed in

@crud_pets.route('/update_species/<name>', methods=['POST', 'GET'])
def update_species(name):
    # find pet based on given pet's name, update pet's species if there's a match
    current_pet = pets_db.db.pets.find_one({"name": name}) # 'find_one()' should convert our PyMongo cursor obj of the record here to an iterable Python dictionary
    current_species = current_pet['species'] # using dictionary properties to get pet's current species
    species_form = NewSpecies(request.form) # get form data KV pairs, assign them to new NewSpecies form object
    if request.method == 'POST':
        # if we're POSTing valid data, let's update the current pet's species
        current_pet['species'] = species_form.new_species.data
        flash('Pet\'s species updated successfully!') # success feedback msg
        return redirect(url_for('index')) # return to home page
    else:
        # if we're not POSTing anything, let's return the regular 'update_species' page
        return render_template('update_species.html', name=name, current_species=current_species, species_form=species_form) # our template with 'update_species' form and 'current_species' variable passed in