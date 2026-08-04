def split_bill_detailed(total, people):
    return total // people, total % people
print(split_bill_detailed(10000, 3))