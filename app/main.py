from flask import Flask, request, jsonify
from .model import simple_ai_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API Flask con IA funcionando"}), 200

@app.route("/ia", methods=["POST"])
def ia():
    data = request.json.get("texto", "")
    respuesta = simple_ai_response(data)
    return jsonify({"respuesta": respuesta})
