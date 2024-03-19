from flask import Blueprint, jsonify

api = Blueprint("api", __name__)


@api.route("/")
def hello_world():
    res = "test"
    return jsonify(res)
