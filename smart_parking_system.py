vehicle = input("Enter vehicle type:").lower()
parking_hours = input("Enter parking hours:")

if parking_hours.isdigit():
    parking_hours = int(parking_hours)
    if vehicle == "bike":
        total_fee = 100 * parking_hours
        print("Total fee:",total_fee, "yen")
    elif vehicle == "car":
        total_fee = 300 * parking_hours
        print("Total fee:",total_fee, "yen")
    elif vehicle == "truck":
        total_fee = 500 * parking_hours
        print("Total fee:",total_fee, "yen")
    else:
        print("Invalid vehicle type")
else:
    print("Invalid parking hours")