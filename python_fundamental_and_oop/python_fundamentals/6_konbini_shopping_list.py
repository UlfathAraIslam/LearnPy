items = ["onigiri", "tea", "bento"]
items.append("pudding")
items.remove("tea")

for index, item in enumerate(items, start=1):
    print(f"{index}.{item}")