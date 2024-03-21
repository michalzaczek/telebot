from flask import Blueprint, jsonify, request
from app.utils import handle_openai_request

api = Blueprint("api", __name__)


@api.route("/")
def hello_world():
    res = "test"
    return jsonify(res)


@api.route("/ask", methods=["POST"])
def ask_openai():
    data = request.json
    messages = data.get("messages", [])

    try:
        response = handle_openai_request(messages)
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
