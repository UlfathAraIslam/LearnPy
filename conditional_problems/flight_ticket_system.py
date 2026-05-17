nationality = input("Enter nationality:").title()
passport = input("Is passport valid?").lower()

if passport == "yes":
    print("Ticket Booking Allowed")
else:
    print("Ticked Booking Denied")