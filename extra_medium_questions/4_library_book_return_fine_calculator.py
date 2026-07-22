fines = []
while True:
    days = int(input("Enter overdue days (-1 to stop):"))
    if days == -1:
        break
    if days <= 0:
        fine = 0
    else:
        fine = days * 5
    fines.append(fine)
total_fines = 0
no_fine_books = 0

i = 0
while i < len(fines):
    total_fines += fines[i]
    
    if fines[i] == 0:
        no_fine_books += 1
    i += 1
print(f"Total fines collected: ¥{total_fines}")
print(f"Books with no fine: {no_fine_books}")