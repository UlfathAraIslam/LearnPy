temperatures = []

while True:
    temp = input("Enter temperature in C (or 'stop'):")
    if temp.lower() == "stop":
        break
    temperatures.append(int(temp))
if len(temperatures) > 0:
    highest = temperatures[0]
    lowest = temperatures[0]
    heat_warnings = 0
    
    i = 0
    while i < len(temperatures):
        if temperatures[i] > highest:
            highest = temperatures[i]
        if temperatures[i] < lowest:
            lowest = temperatures[i]
        if temperatures[i] > 35:
            heat_warnings += 1
        i += 1
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Heat warnings (>35C): {heat_warnings}")
else:
    print("No temperature readings entered.")