import re

email = input("Email? ").strip()

if re.search(r"^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
  print("Valid")
else:
  print("Invalid")
