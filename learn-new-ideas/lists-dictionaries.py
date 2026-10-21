prices = [850, 230, 4800]
prices.append(600)
print(prices)
print(len(prices))
# ()
person = {"name": "Rina","city": "Osaka"}
print(person["city"])
person["age"]= 24
print(person.get("phone", "none"))

fruits = ["apple","banana","mango"]
for index, fruit in enumerate(fruits):
    print(index,fruit)
removed = fruits.pop(1)
print(removed)
print(fruits)