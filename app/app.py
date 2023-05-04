from flask import Flask, request
from lib.utils import get_env_or_die, json_response
from meta.envs import Envs
from meta.logo import logo
from meta.status import Status
from lib.migrate import Migrate
from data.schema import get_schema
from data.seed import seed_admin
from api.authentic import authentic

API_VERSION = 0.1

for e in Envs:
    get_env_or_die(e.value)

migrate = Migrate()
migrate.run(get_schema())
seed_admin()

logo(API_VERSION)

app = Flask(__name__)
app.secret_key = 'super secret key'
app.register_blueprint(authentic)

@app.before_request
def only_json():
    if not request.is_json: 
        return json_response(Status.Failed, "content-type: application/json required")
        
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"