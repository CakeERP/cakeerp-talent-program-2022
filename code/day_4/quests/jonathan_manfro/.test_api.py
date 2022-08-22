from .config import *

def test_status():
    response = client.get("/status")
    assert response.status_code == 200