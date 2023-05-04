from typing import TypedDict
from enum import Enum
from meta.fields import Fields
class AccountType(Enum):
    Admin="admin"
    Standard="standard"
class User(TypedDict):
    first_name: str
    last_name: str
    email: str
    password: str
    type: str

class UpdateUser(TypedDict):
    id: str
    first_name: str
    last_name: str
    email: str

def create_new_user_query(user, db):
  sql = """
    INSERT INTO SYSTEM_USER (
      email,
      first_name,
      last_name,
      password,
      type,
      active,
      date_added
    ) VALUES (
      %(email)s, 
      %(first_name)s, 
      %(last_name)s,
      %(password)s,
      %(type)s,
      false,
      now()
    )
  """

  return db.exec_db(sql, {
    "email": user.get(Fields.Email.value),
    "first_name": user.get(Fields.FirstName.value),
    "last_name": user.get(Fields.LastName.value),
    "password": user.get(Fields.Password.value),
    "type": user.get(Fields.Type.value)
  })

def update_user_query(user, db):
  sql = """
    UPDATE 
      SYSTEM_USER
    SET
      first_name = %(first_name)s,
      last_name  = %(last_name)s,
      email = %(email)s,
      last_updated = now()
    WHERE
      id = %(id)s
  """
  return db.exec_db(sql, {
    "id": user.get(Fields.Id.value),
    "first_name": user.get(Fields.FirstName.value),
    "last_name": user.get(Fields.LastName.value),
    "email": user.get(Fields.Email.value),
  })


def get_user_by_email_query(email, db):
  sql = "SELECT * FROM SYSTEM_USER WHERE email = %(email)s;"
  return db.run_db(sql, { "email": email})

def get_user_by_id_query(id, db):
  sql = "SELECT * FROM SYSTEM_USER WHERE id = %(id)s;"
  return db.run_db(sql, { "id": id})
