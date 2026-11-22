
from pathlib import Path
import sys

from fastapi.testclient import TestClient

# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parents[1]
print(ROOT_DIR)
sys.path.insert(0, str(ROOT_DIR))

from main import app

client = TestClient(app)


def test_root_endpoint():
    response_01 = client.get("/health")

    assert response_01.json() == {"Status":"Running","application":"DataPilot"}

def test_db_connection():
    response_02 = client.get("/DBHealth")

    assert response_02.json() == {"DB":"postgres","status":"live"}

