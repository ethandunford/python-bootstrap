from flask import session
import data.user
from core.app import validate
from meta.fields import Fields
from lib.validation import is_email, is_password

def start_system_session(id, first_name, last_name):
   session["user"] = { 
     "id": id,
     "first_name": first_name,
     "last_name": last_name,
  }

def clear_system_session():
   if session and session["user"]:
      session.clear()

def get_system_session():
   if session and session["user"]:
      return session["user"]

def validate_auth(raw):
   errors = []
   errors = validate(raw, Fields.Email,         is_email,         "invalid email",            errors)
   errors = validate(raw, Fields.Email,         is_email,         "invalid email",            errors)
   errors = validate(raw, Fields.Password,      is_password,      "invalid password",         errors)
   return errors

def get_data(email, db):
   return data.user.get_user_by_email_query(email, db)