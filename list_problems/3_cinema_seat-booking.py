#3
'''
-starts with Given seats = [10, 11, 12, 13, 14, 15, 16].
-Use seats[0] for first seat
-use seats[-1] for last seat.
-print first and last seat
-slice 3 seats using seats[2:5].
-store these 3 seats as booked-seats
-print booked-seats
-check booking
- if booked seats == 3 print confirmation
-else print booking failed
'''
seats = [10, 11, 12, 13, 14, 15, 16]
first_seat = seats[0]
last_seat = seats[-1]
print(f"First seat:{first_seat} | Last seat:{last_seat}")
booked_seats = seats[2:5]
print("Booked seats:",booked_seats)
if(len(booked_seats) == 3):
    print("Booking confirmed for 3 seats!")
else:
    print("Booking failed")