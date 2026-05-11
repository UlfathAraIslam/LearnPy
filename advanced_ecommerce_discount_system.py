membership = input("Are you a member?(yes/no):").lower()
cart_amount = input("Enter amount:")

if cart_amount.isdigit():
    cart_amount = float(cart_amount)

    if membership == "yes":
        if cart_amount >= 20000:
            discount = cart_amount * 0.03
        elif cart_amount >= 10000:
            discount = cart_amount * 0.02
        else:
            discount = cart_amount * 0.01

        final_bill = cart_amount - discount
        print("Final bill:",final_bill)

    else:
        print("No discount")
        print("Final bill:",cart_amount)
else:
    print("Invalid")