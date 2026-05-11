quantity = input("Enter quantity:")

if quantity.isdigit():
    quantity = int(quantity)
    if quantity >0:
        print("In Stock")
    else:
        print("Out of Stock")