# shortcut loop
prices = [850, 230, 4800]
doubled = []
for p in prices:
    doubled.append(p * 2)

#  in one line
doubled = [p * 2 for p in prices]
print(doubled)

print(sum(p for p in prices))