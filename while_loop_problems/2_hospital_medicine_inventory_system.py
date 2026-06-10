#2
'''
-names = []
-quantities = []
-prices = []
-while True:
-ask medicine name input . title()
-name =="done"
-break to stop loop
-store name in list using append
-ask quantity -> int()
-store quantity in list using append
-ask price -> float()
-store price in list using append
-after input end, print inventory report
-use while loop with index
-For each medicine, calculate total value (quantity x unit price)
-check stock status:
-quantity >= 100 → 'Sufficient', quantity >= 50 → 'Low', below 50 → 'Critical'
-check highest value with max()
'''
names = []
quantities = []
prices = []
# Data storing
while True:
    medicine_name = input("Enter medicine name (or 'done'):").title()
    if medicine_name == "Done":
        break
    else:
        names.append(medicine_name)
        quantity = int(input("Enter quantity:"))
        quantities.append(quantity)
        price = float(input("Enter unit price:"))
        prices.append(price)
# Data access 
print('''
==========================================================
PHARMACY INVENTORY REPORT
==========================================================
Medicine | Qty | Unit Price | Total Value | Status
----------------------------------------------------------
''')
# use while loop with index to print the table 
highest_value = 0
highest_medicine = ""
index = 0
while index < len(names):
    current_name = names[index]
    current_quantity = quantities[index]
    current_price = prices[index]
    total_value = current_quantity * current_price
    #check status
    if current_quantity >=100:
        status = "Sufficient"
    elif current_quantity >= 50:
        status ="Low"
    else:
        status="Critical"
    #print inventory row
    print(
    f"{current_name} | "
    f"{current_quantity} | "
    f"{current_price} | "
    f"{total_value} | "
    f"{status}"
      )
    #check highest value stock
    if total_value > highest_value:
        highest_value = total_value
        highest_medicine = current_name
    index += 1
# after while loop ends
print("----------------------------------------------------------")
print(f"Highest value stock: {highest_medicine} ({highest_value} yen)")