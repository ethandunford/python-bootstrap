import pytest
import json
from lib.requests import post, post_session, start_session
from lib.utils import get_env


URL     = get_env('API_URL')
HEADERS = '{"content-type": "application/json"}'

@pytest.fixture
def client():
    return

def test_user_login(client):
  payload = {
    "action": "login",
    "email": "admin@test.com",
    "password": "Password1!"
  }

  raw       = post(url=f"{URL}/authentic", payload=json.dumps(payload), headers=HEADERS)
  response  = json.loads(raw["body"])
  assert response["status"] == "ok"


def test_user_login(client):
  payload = {
    "action": "login",
    "email": "admin@test.com",
    "password": "Password"
  }

  raw       = post(url=f"{URL}/authentic", payload=json.dumps(payload), headers=HEADERS)
  response  = json.loads(raw["body"])
  assert response["status"] == "failed"
  assert response["data"] == "email or password is incorrect"

def test_user_get_session(client):
    r = start_session()
    r = post_session(url=f"{URL}/authentic", session=r, payload=json.dumps({"action": "get_session"}), headers=HEADERS)
    response1 = json.loads(r["body"])
    assert response1["status"] == "unauthenticated"

    payload = {
        "action": "login",
        "email": "admin@test.com",
        "password": "Password1!"
    }

    r = post_session(url=f"{URL}/authentic", session=r["session"], payload=json.dumps(payload), headers=HEADERS)
    response2 = json.loads(r["body"])
    assert response2["status"] == "ok"

    r = post_session(url=f"{URL}/authentic", session=r["session"], payload=json.dumps({"action": "get_session"}), headers=HEADERS)
    response3 = json.loads(r["body"])
    assert response3["status"] == "ok"