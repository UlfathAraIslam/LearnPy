def update_inventory(stock, sold, threshold=5, restock=10):
    updated = []
    for s,so in zip(stock, sold):
        remaining = stock - sold
        if remaining < threshold:
            remaining += restock
        updated.append(remaining)
    return updated