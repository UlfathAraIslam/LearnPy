recharge_amount = (input("Enter recharge amount:"))

if recharge_amount.isdigit():
    recharge_amount = int(recharge_amount)
if recharge_amount > 1000:
    print (100,"yen")
else:
    print("No Bonus")