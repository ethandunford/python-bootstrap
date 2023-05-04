import requests
import json
from lib.utils import log
from meta.result import Status, HttpResult

def log_response(code: int, response: str):
    log(f"[RESPONSE][RAW][{code}]")
    log(response)


def post(**kwargs) -> HttpResult:
    try:
        r = requests.post(kwargs.get("url"), data=kwargs.get("payload"), files=kwargs.get("files"), headers=json.loads(kwargs.get("headers", {})))
        log_response(r.status_code, r.text)
        return HttpResult(status=Status.Ok.value, httpCode=r.status_code, body=r.text, error=None)
    except Exception as e:
        log(e)
        return HttpResult(status=Status.Error.value, httpCode=400, body=None, error=None)


def get(**kwargs) -> HttpResult:
    try:
        r = requests.get(kwargs.get("url"))
        log_response(r.status_code, r.text)
        return HttpResult(status=Status.Ok.value, httpCode=r.status_code, body=r.text, error=None)
    except Exception as e:
        log(e)
        return HttpResult(status=Status.Error.value, httpCode=400, body=None, error=None)


def start_session():
    return requests.Session()


def post_session(session, **kwargs):
    try:
        r = session.post(kwargs.get("url"), data=kwargs.get("payload"), files=kwargs.get("files"), headers=json.loads(kwargs.get("headers", {})))
        log_response(r.status_code, r.text)
        return HttpResult(status=Status.Ok.value, httpCode=r.status_code, body=r.text, error=None, session=session)
    except Exception as e:
        print(e)
        return HttpResult(status=Status.Error.value, httpCode=400, body=None, error=None, session=session)
