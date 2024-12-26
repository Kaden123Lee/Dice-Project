# makes website folder a package 
from flask import Flask 

def create_app():
    app = Flask(__name__) # How it initilizes flask just the syntax thats all 
    app.config['SECRET_KEY'] = '3n9imcf340ij34c0i2j340cij340ij2345n-x-234n4n234jnx' # for encripting the session and cookies data

    from .views import views 
    from .auth import auth 

    app.register_blueprint(views, url_prefix='/') # all urls that are stored in this file how to access them 
    app.register_blueprint(auth, url_prefix='/') # goes to the routes you defined in the files 
    return app 