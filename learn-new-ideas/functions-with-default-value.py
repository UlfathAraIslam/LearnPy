def greet(name, greeting="Hello"):
    return greeting + ", " + name + "!"

print(greet("Rahim"))
print(greet("Rahim", "Salam"))

def show_date(when=None):
    if when is None:
        return "today"
    return when
print(show_date())
print(show_date("2026-10-01"))