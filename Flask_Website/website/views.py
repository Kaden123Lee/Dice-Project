from flask import Blueprint 
# seprate our app out and stuff 
views = Blueprint('views', __name__)

@views.route("/") #to define a route
def home():
    return "<h1>Test</h1>"