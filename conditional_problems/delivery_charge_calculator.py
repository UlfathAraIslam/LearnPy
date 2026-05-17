shopping_amount = input("Enter amount:")

if (shopping_amount).isdigit():
    shopping_amount = int(shopping_amount)
    if(shopping_amount> 5000):
        print("Free delivery")
    else:
        print("Delivery Charge: 500 yen")
else:
    print("Invalid")