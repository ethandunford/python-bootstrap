from lib.db import Db
from lib.utils import get_env, log

db = Db(get_env("DB"))

def seed_admin():
  if int(get_env("DEBUG")) == 1:
    log("seeding admin")
    db.exec_db("DELETE FROM SYSTEM_USER WHERE email = 'admin@test.com';")
    db.exec_db(""" 
      INSERT INTO SYSTEM_USER (
        email,
        first_name,
        last_name,
        password,
        type, 
        active,
        date_added
      ) VALUES (
        'admin@test.com',
        'admin',
        'admin',
        '$2b$12$cFiJv4eJ4FRuOqjqz1QG2ejUEj8VW1uI6vxxhBw08LVbuV.UtsFoq',
        'admin',
        true,
        now()
      );
      """
    )