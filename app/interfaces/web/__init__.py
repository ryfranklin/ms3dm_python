from flask import Blueprint, jsonify

bp = Blueprint('web', __name__)

@bp.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Page not found"}), 404

@bp.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal server error"}), 500

@bp.route('/')
def index():
    return 'Hello, world!'
