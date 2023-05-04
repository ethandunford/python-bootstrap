from flask import Blueprint, request
from bcrypt import checkpw
import core.authentic
from lib.utils import json_response, get_env
from lib.db import Db
from meta.status import Status
from meta.fields import Fields
from meta.result import Status

authentic = Blueprint('api_authentic', __name__)
db = Db(get_env("DB"))

@authentic.route('/authentic', methods=['POST'])
def process():
    try:
        raw = request.get_json()
    except Exception:
        return json_response(Status.Failed, "json invalid")

    action = raw.get(Fields.Action.value, None)
    match action:
        case "login":
            return login(raw, db)
        case "logout":
            return logout(raw)
        case "get_session":
            return get_session(raw)
        case _:
            return json_response(Status.Failed, "unknown action")


def login(raw, db):

    errors = core.authentic.validate_auth(raw) 

    if errors:
        return json_response(Status.Error, errors)
    
    login_data = core.authentic.get_data(raw.get(Fields.Email.value), db)
    
    if login_data.get("status") != Status.Ok:
        return json_response(Status.Failed, "failed to login")

    if len(login_data.get("data")) == 0:
        return json_response(Status.Failed, "email or password is incorrect")
    
    if checkpw(raw.get(Fields.Password.value).encode('utf-8'), login_data.get("data")[0][Fields.Password.value].encode('utf-8')) is False:
        return json_response(Status.Failed, "email or password is incorrect")
    
    core.authentic.start_system_session(
      login_data.get("data")[0][Fields.Id.value],
      login_data.get("data")[0][Fields.FirstName.value],
      login_data.get("data")[0][Fields.LastName.value],
    )

    return json_response(Status.Ok, None)

def logout(raw):
    core.authentic.clear_system_session()
    return json_response(Status.Unauthenticated, None)

def get_session(raw):
    s = core.authentic.get_system_session()
    if s:
        return json_response(Status.Ok, s)
    return json_response(Status.Unauthenticated, None)