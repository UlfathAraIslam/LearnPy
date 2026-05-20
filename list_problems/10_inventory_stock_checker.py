#10
'''
-start with quantities:[0, 5, 12, 0, 3]
-print total products
-print the max()and min() for stock extremes
-replace stock[0]= 8
-print updated list
'''
#* Review names
product_quantities= [0, 5, 12, 0, 3]
print("Total products:",len(product_quantities))
print(f"Max stock: {max(product_quantities)} | Min stock: {min(product_quantities)}")
product_quantities[0]=8
print("Updated stock:",product_quantities)
