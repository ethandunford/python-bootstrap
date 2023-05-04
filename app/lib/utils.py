from time import strftime, time
from meta.status import Status
import os
import sys
import json

def log(msg: str):
    print("".join(("[", strftime("%Y-%m-%d %H:%M:%S"), "] ==> ", msg)), flush=True)

def get_env(env: str) -> str:
    if env in os.environ:
        return os.environ[env]
    else:
        log("".join(("Exiting missing environment variable => ", env)))
    return ""

def get_env_or_die(env: str):
    if env in os.environ:
        return os.environ[env]
    else:
        log("".join(("Exiting missing environment variable => ", env)))
        sys.exit(0)

def json_response(status: Status, data) -> str:
    return json.dumps({"status": status.value, "data": data}, sort_keys=True, default=str)