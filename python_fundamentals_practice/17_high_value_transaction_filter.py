def cashback_points(transactions):
    return [amt // 500 for amt in transactions if amt >= 1000]
print(cashback_points([500, 1200, 3000, 800, 1500]))