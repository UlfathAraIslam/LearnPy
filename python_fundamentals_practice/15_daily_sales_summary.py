def sales_summary(sales):
    total = 0
    for sale in sales:
        total += sale
    average = total / len(sales)
    days_above_average = 0
    for sale in sales:
        if sale > average:
            days_above_average += 1
    return total, days_above_average
print(sales_summary([12000, 8000, 15000, 9000]))