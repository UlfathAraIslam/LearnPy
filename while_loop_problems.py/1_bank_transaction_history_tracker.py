#1
'''
-start with
--start_balance = 100000
--transaction_types = []
--transaction_amounts = []
--deposit_count = 0
--withdraw_count = 0
-while True
--transaction_type : Enter transaction type (deposit/withdraw or 'done'):
--upper()
-if transaction_type == done:
--break
--transaction_amount : Enter amount:
-if transaction_type == deposit:
-- add amount to balance
--store in lists with append type and amount
--increase deposit count
-if transaction_type == withdraw:
--if amount > balance:
--print rejection msg
--else:
--subtract from balance
--store in lists by append
--increase withdrawal count
-else:
--print invalid transaction
-use while loop with index to print history table
'''
balance = 100000
transaction_types = []
transaction_amounts = []
deposit_count = 0
withdraw_count = 0
print(f"Opening Balance:{balance}")
while True:
    transaction = input("Enter transaction type (deposit/withdraw or 'done'):").upper()
    if transaction == "DONE":
        break
    amount = int(input("Enter amount:"))
    #deposit
    if transaction =="DEPOSIT":
        #increment
        balance +=amount
        #store in lists
        transaction_types.append(transaction)
        transaction_amounts.append(amount)
        #increase counter
        deposit_count += 1
    #withdraw
    elif transaction == "WITHDRAW":
        #check balance
        if amount >balance:
            print("Rejected: Insufficient balance")
        else:
            #decrement
            balance -= amount
            #store in lists
            transaction_types.append(transaction)
            transaction_amounts.append(amount)
            #increase counter
            withdraw_count += 1
    else:
        print("Invalid transaction type")
# print history
print("===================================")
print("TRANSACTION HISTORY")
print("===================================")
print("No. | Type | Amount | Balance")
print("------------------------------------")

running_balance = 100000
index = 0
# while loop for history
while index < len(transaction_types):
    current_type = transaction_types[index]
    current_amount = transaction_amounts[index]
    # deposit history
    if current_type == "DEPOSIT":
        running_balance += current_amount
        print(f"{index + 1} | {current_type} | +{current_amount} | {running_balance}")
    # withdraw history
    else:
        running_balance -= current_amount
        print(f"{index + 1} | {current_type} | -{current_amount} | {running_balance}")
    index += 1
print("------------------------------------")
print("Total Deposits:",deposit_count)
print("Total Withdrawals:",withdraw_count)
print("Closing Balance:",balance)