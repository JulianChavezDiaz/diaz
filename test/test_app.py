from app.main import app

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200

def test_ia():
    client = app.test_client()
    res = client.post("/ia", json={"texto": "hola"})
    data = res.get_json()
    assert "Hola" in data["respuesta"]
