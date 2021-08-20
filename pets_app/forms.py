
from flask_wtf import FlaskForm # all our web forms inherit from here
from wtforms import StringField, IntegerField, TextAreaField, SelectField, SubmitField, validators # fields/modules needed for our forms

class AddPet(FlaskForm):
    name = StringField('Name', [validators.DataRequired()]) # pet's name, can't be empty
    species = StringField('Species', [validators.DataRequired()]) # pet's species, can't be empty
    age = IntegerField('Age (in years)', [validators.DataRequired()]) # pet's age in years, can't be empty
    sex = SelectField('Sex/Gender', [validators.DataRequired()], choices=[('M', 'Male'), ('F', 'Female')]) # pet's sex/gender (male or female), can't be empty
    description = TextAreaField('Description', [validators.DataRequired()]) # description of pet, can't be empty
    submit = SubmitField('Add Pet') # 'submit' button for form

# all updating forms

class NewName(FlaskForm):
    new_name = StringField('Name', [validators.DataRequired()]) # pet's name, can't be empty
    submit = SubmitField('Done') # 'submit' button for form

class NewSpecies(FlaskForm):
    new_species = StringField('Species', [validators.DataRequired()]) # pet's species, can't be empty
    submit = SubmitField('Done') # 'submit' button for form

class NewAge(FlaskForm):
    new_age = IntegerField('Age (in years)', [validators.DataRequired()]) # pet's age in years, can't be empty
    submit = SubmitField('Done') # 'submit' button for form

class NewGender(FlaskForm):
    new_sex = SelectField('Sex/Gender', [validators.DataRequired()], choices=[('M', 'Male'), ('F', 'Female')]) # pet's sex/gender (male or female), can't be empty
    submit = SubmitField('Done') # 'submit' button for form

class NewDescription(FlaskForm):
    new_description = TextAreaField('Description', [validators.DataRequired()]) # description of pet, can't be empty
    submit = SubmitField('Done') # 'submit' button for form