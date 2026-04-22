class PasswordError(Exception):
    pass

def validate(p):
    if len(p) < 8:
        raise PasswordError("Too short")
    if not any(c.isupper() for c in p):
        raise PasswordError("Missing uppercase")
    if not any(c.islower() for c in p):
        raise PasswordError("Missing lowercase")
    if not any(c.isdigit() for c in p):
        raise PasswordError("Missing digit")

try:
    pwd = input("Enter password: ")
    validate(pwd)
    print("Valid password")
except PasswordError as e:
    print("Error:", e)