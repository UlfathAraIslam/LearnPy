#8
# Store total members
total_members = 0

# Store total revenue
total_revenue = 0

# Infinite loop
while True:

    # Take member name
    name = input("Enter member name (or 'stop' to exit): ").lower()

    # Stop program if user enters stop
    if name == "stop":
        break

    # Take member age
    age = int(input("Enter age: "))

    # Take membership plan
    plan = input("Enter plan (basic/premium/vip): ").lower()

    # Select fee based on plan

    if plan == "basic":
        fee = 2000

    elif plan == "premium":
        fee = 4000

    elif plan == "vip":
        fee = 7000

    else:
        print("Invalid plan")

    # Default discount
    discount = 0

    # Senior discount
    if age >= 60:

        discount = 20

    # Student discount
    elif age <= 15:

        discount = 30

    # Calculate payable amount

    payable = fee - (fee * discount / 100)

    # Print member details

    print(
        f"{name.title()} -> "
        f"Plan: {plan} | "
        f"Fee: {fee} | "
        f"Discount: {discount}% | "
        f"Payable: {payable}"
    )

    # Increase member count
    total_members += 1

    # Add payable amount to revenue
    total_revenue += payable

# Print final summary

print("Total members:", total_members)
print("Total revenue:", total_revenue)