def process_transactions(start_balance, transactions):
    balance = start_balance
    skipped_indices = []

    i = 0
    while i < len(transactions):
        transaction = transactions[i]
        if balance + transaction < 0:
            skipped_indices.append(i)
        else:
            balance += transaction
        i += 1
    return balance,skipped_indices

start_balance = 500
transactions = [200, -100, -700, 50, -1000]
print(process_transactions(start_balance,transactions))