from flask import Blueprint

hello_world_bp = Blueprint('hello world', __name__)

# using the blueprint decorator: 
# @@blueprint_name.route("/endpoint/path/here", methods=["GET"])
@hello_world_bp.route('/hello-world', methods=["GET"])
def get_hello_world():
    my_response = "Hello, World!"
    return my_response

