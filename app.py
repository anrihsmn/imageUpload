from flask import Flask, session
from .database import init_db   #.database.py 
from .config import Config   #config.py 
from . import models    #models package 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # IF NO SECRET KEY
    # RuntimeError: The session is unavailable because no secret key was set.  
    # Set the secret_key on the application to something unique and secret.
    # secret_key binds your application and your session variables

    app.secret_key = "abc"  

    init_db(app)


    return app 

app = create_app()

