units = input ("Enter units:")

if units.isdigit():
    units = int(units)
    
    if units > 500:
        print("High bill")
    else:
        print("Normal bill")