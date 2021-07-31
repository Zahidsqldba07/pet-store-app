
from pets_app import pets_app # importing our app obj from app pkg

if __name__ == '__main__':
    pets_app.run(debug=True) # if __name__ = current module (run.py), we run the app on local server with debug = true
    # this makes sure server restarts upon code changes