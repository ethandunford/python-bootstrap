import re

def is_email(s: str) -> bool:
  if not re.match("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", s):
    return False
  return True

def is_name(s: str) -> bool:
  if not re.match("[A-Za-z]{2,25}( [A-Za-z]{2,25})?", s):
    return False
  return True

def is_password(s: str) -> bool:
  if len(s) < 6:
    return False
  return True

def is_not_empty_or_none(s: str) -> bool:
    s = str(s)
    if s is None:
        return False
    if len(s) == 0:
        return False
    return True

def is_number(s: str) -> bool:
  try:
    return str(s).isnumeric()
  except:
    return False