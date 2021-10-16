from flask import Blueprint

hello_world_bp = Blueprint('hello_world', __name__)

# using the blueprint decorator: 
# @@blueprint_name.route("/endpoint/path/here", methods=["GET"])
@hello_world_bp.route('/hello-world', methods=["GET"])
def get_hello_world():
    my_response = "Hello, World!"
    return my_response

@hello_world_bp.route('/hello-world/JSON', methods=["GET"])
def hello_world_json():
    return {
        'name': 'jollyranger',
        'message': 'Helloooooo!!',
        'hobbies': ['fishing', 'laughing', 'drinking']
        
    }, 201

