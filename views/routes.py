from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api/v1')

@api.route('/health')
def health():
    return jsonify({"status": "ok"})

@api.route('/todos', methods=['GET'])
def get_todos():
    return jsonify([])

