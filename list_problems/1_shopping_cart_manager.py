#1
'''
- take an empty array to put items name
-input string items 3 times
-append each item in the empty array
-store all append items in a cart
-print the list of items
-print the count

'''

items = []
item1 = input("Enter item 1:")
item2 = input("Enter item 2:")
item3 = input("Enter item 3:")
items.append(item1)
items.append(item2)
items.append(item3);
your_cart = items;
print("Your cart:",your_cart)
print("Total items:",len(items))