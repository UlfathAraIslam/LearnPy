age = 20
label = "adult" if age >= 18 else "child"
print(label)

when = None
print(when or "today")

for n in [1,2,3,4]:
    if n % 2 == 0:
        continue
    print(n)