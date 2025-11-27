def simple_ai_response(texto: str) -> str:
    texto = texto.lower()

    if "hola" in texto:
        return "Hola, ¿cómo puedo ayudarte?"
    if "adios" in texto or "chao" in texto:
        return "Hasta luego!"
    
    return "No entiendo tu mensaje, pero estoy aprendiendo 😄"
