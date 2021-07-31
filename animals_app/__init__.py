
# basically just initialize our app and DB here

from flask import Flask, render_template # importing Flask obj to make app and 'render_template' module to render HTML templates

animals_app = Flask(__name__) # initializing our app obj

from dotenv import load_dotenv # importing 'load_dotenv()' to load our env variables
import os # importing Python library for interfacing with OS
load_dotenv()

animals_app.config["MONGO_URI"] = os.getenv("MONGO_URI") # configuring our DB location

@animals_app.route('/')
@animals_app.route('/index')
def index():
    return "This is a homepage!"

