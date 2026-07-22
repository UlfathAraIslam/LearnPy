bookings = []
while True:
    tickets = int(input("Enter number of tickets (0 to stop):"))
    if tickets == 0:
        break
    amount = tickets * 150
    bookings.append(amount)
total_revenue = 0
highest_booking = 0

i = 0
while i< len(bookings):
    total_revenue += bookings[i]

    if bookings[i] > highest_booking:
        highest_booking = bookings[i]

    i += 1

print(f"Total revenue: ¥{total_revenue}")
print(f"Highest booking amount: ¥{highest_booking}")