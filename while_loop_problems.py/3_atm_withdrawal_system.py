#3
'''
-start with balance = 50000
-while True:
-ask withdrawal amount (0 to exit):
-int() to convert input
-if amount <= 0, break, exit the loop
-check balance
-If amount > balance, print 'Insufficient funds
-else:
-remaining_balance = balance - amount
-print remaining balance
'''
balance = 50000
print("Balance:",balance)
while True:
    amount = int(input("Enter withdrawal amount (0 to exit):"))
    if amount<= 0:
        break
    elif amount> balance:
            print("Insufficient funds.")
    else:
        remaining_balance = balance - amount
        print(f"Withdrawal successful. Remaining balance: {remaining_balance}")
print(f"Thank you! Final balance: {remaining_balance}")
