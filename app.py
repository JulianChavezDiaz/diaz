from flask import Flask, request, jsonify
from model import simple_ai_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API Flask con IA funcionando"}), 200

@app.route("/ia", methods=["POST"])
def ia():
    data = request.json.get("texto", "")
    respuesta = simple_ai_response(data)
    return jsonify({"respuesta": respuesta})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1002)  