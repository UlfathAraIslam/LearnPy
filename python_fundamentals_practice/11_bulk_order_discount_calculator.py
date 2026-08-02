def bulk_discount_total(prices):
    total = sum(prices)
    count = len(prices)
    if count >= 10:
        total *= 0.8
    elif count >=5:
        total *= 0.9
    return int(total)
print(bulk_discount_total([500, 700, 300, 900, 600]))