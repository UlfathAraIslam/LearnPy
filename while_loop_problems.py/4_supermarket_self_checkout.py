#4
'''
-take empty array to store
-products=[]
-prices =[]
-while True:
-ask for product name --input
-if product_name == "done":---break
-else
-append product_name in products
-ask for price --input-float
-append price in prices
-print total items len(products)
-sum(prices)--for total bill
'''
products = [] # creates an empty list to store product names
prices = [] # creates an empty list to store product prices
index = 0 # creates a variable to access list items one by one
while True: # runs again and again until break is used
    product_name = input("Enter product (or 'done' to finish):").lower() # take user input, convert text to lower case
    if product_name == "done": # check did user type done ,if yes-stop
        break
    else: # if user did not type done, then run the following code
        products.append(product_name) # add items to list
        product_price = float(input("Enter price:")) # takes price from user, convert to decimal number
        prices.append(product_price) # add price to list
# loop ended after user typed done
print("--- Your Receipt ---")
# receipt printing loop
while index < len(products): # keep looping while index is smaller than total products
    print (f"{products[index]} : {prices[index]}")
    index += 1 # increase index each loop
# condition false -> loop stops
print(f"Total items: {len(products)}")
print(f"Total bill: {sum(prices)}")