from dataclasses import dataclass, asdict

@dataclass
class Student:
    name: str
    age: int
    city: str = "Osaka"
s = Student("Rahim",24)
print(s.name)
print(s.city)
print(asdict(s))
info = {"name": "Karim", "age": 30}
k = Student(**info)
print(k)