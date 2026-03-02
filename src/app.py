"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_get_members():
    """Return a list with all family members."""
    members = jackson_family.get_all_members()
    return jsonify(members), 200


@app.route('/members', methods=['POST'])
def handle_add_member():
    """Create a new member using JSON payload and return it."""
    data = request.get_json()
    if not data:
        raise APIException("Invalid payload", status_code=400)
    member = jackson_family.add_member(data)
    return jsonify(member), 200


@app.route('/members/<int:member_id>', methods=['GET'])
def handle_get_member(member_id):
    """Retrieve a single family member by id."""
    member = jackson_family.get_member(member_id)
    if member is None:
        raise APIException("Member not found", status_code=404)
    return jsonify(member), 200


@app.route('/members/<int:member_id>', methods=['DELETE'])
def handle_delete_member(member_id):
    """Delete a member and return a simple confirmation object."""
    success = jackson_family.delete_member(member_id)
    if not success:
        raise APIException("Member not found", status_code=404)
    return jsonify({"done": True}), 200

# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
