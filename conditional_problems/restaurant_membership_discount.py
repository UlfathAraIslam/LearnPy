member = input("Are you a member? (yes/no):").lower()
bill_amount = float(input("Total bill amount:"))


final_bill = bill_amount * 0.90 if member ==("yes") else bill_amount

print("final bill:",final_bill)
