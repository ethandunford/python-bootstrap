import string
import random

def random_string():
  return ( ''.join(random.choice(string.ascii_lowercase) for i in range(10)) )

def random_first_name():
  names = [
  "Liam",
  "Noah",
  "Oliver",
  "Elijah",
  "James",
  "William",
  "Benjamin",
  "Lucas",
  "Henry",
  "Theodore",
  "Olivia",
  "Emma",
  "Charlotte",
  "Amelia",
  "Ava",
  "Sophia",
  "Isabella",
  "Mia",
  "Evelyn",
  "Harper"
  ]

  return random.choice(names)

def generate_email():
  return f"{random_first_name()}@{random_string()}.com"