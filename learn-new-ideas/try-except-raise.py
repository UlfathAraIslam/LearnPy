text = "abc"
try:
    number = int(text)
    print("Got", number)
except ValueError:
    print("That is not a number")

class AgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative.")
    return age
try:
    check_age(-5)
except AgeError as error:
    print("Error:", error)