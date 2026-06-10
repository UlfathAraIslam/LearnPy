'''
START
   |
   v
Create empty inventory list
   |
   v
Start input loop
   |
   v
Input product name
   |
   +----> name == "done" ?
   |             |
   | YES         v
   |----------> BREAK
   |
   v
Input category
Input quantity
Input price
   |
   v
Format text
(title and upper)
   |
   v
Append record to inventory
   |
   v
Repeat input loop
   |
   v
Start inventory while loop
   |
   v
Get product details
   |
   +--> Calculate total value
   |
   +--> Classify stock
   |
   +--> Print product info
   |
   +--> Check highest value
   |
   v
Next product
   |
   v
Print highest value product
   |
   v
END
'''


# Step 1: Create empty inventory list
inventory = []

#* Input in while loop

while True:

    # Ask product name
    name = input("Enter product name (or 'done'): ")


    # Check exit condition
    if name.lower() == "done":

        break


    # Ask category
    category = input("Enter category: ")


    # Ask quantity
    quantity = int(input("Enter quantity: "))


    # Ask unit price
    unit_price = float(input("Enter unit price: "))


    # Format product name using title()
    name = name.title()


    # Format category using upper()
    category = category.upper()


    # Store record in inventory list
    inventory.append([name, category, quantity, unit_price])

# REPORT SECTION

print("=============================================================")
print("WAREHOUSE INVENTORY REPORT")
print("=============================================================")

print("Product | Category | Qty | Unit Price | Total Value | Stock")

print("-------------------------------------------------------------")


# Variable to track highest stock value
highest_value = 0


# Variable to track highest product
highest_product = ""

#* WHILE LOOP TO PRINT INVENTORY


i = 0

while i < len(inventory):


    # Get values using indexing
    product_name = inventory[i][0]

    category = inventory[i][1]

    quantity = inventory[i][2]

    unit_price = inventory[i][3]


    # Calculate total stock value
    total_value = quantity * unit_price


    # STOCK LEVEL CLASSIFICATION

    if quantity >= 100:

        stock_level = "High"


    elif quantity >= 50:

        stock_level = "Medium"


    else:

        stock_level = "Low"


    # Print product details
    print(
        f"{product_name} | {category} | {quantity} | "
        f"{unit_price} | {total_value} | {stock_level}"
    )

    # CHECK HIGHEST VALUE PRODUCT

    if total_value > highest_value:

        highest_value = total_value

        highest_product = product_name


    # Move to next product
    i = i + 1

# FINAL REPORT

print("-------------------------------------------------------------")

print(
    f"Highest value product: "
    f"{highest_product} ({highest_value} yen)"
)
