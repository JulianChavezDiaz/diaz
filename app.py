from flask import Flask, request, jsonify

app = Flask(__name__)

def simple_ai_response(texto: str) -> str:
    """Función integrada - sin dependencias externas"""
    texto = texto.lower()
    
    if "hola" in texto:
        return "Hola, ¿cómo puedo ayudarte?"
    if "adios" in texto or "chao" in texto:
        return "Hasta luego!"
    if "nombre" in texto:
        return "Me llamo Diaz AI"
    
    return "No entiendo tu mensaje, pero estoy aprendiendo 😄"

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