'''
START
   |
Create rooms 2D list
   |
   v
Set total_booked = 0
Set total_revenue = 0
   |
   v
Display all rooms using while loop
   |
   v
Start booking loop
   |
   v
Ask user for room number
   |
   +------> If input = 0
   |              |
   |              v
   |            BREAK
   |
   v
Check valid room number
   |
   +------> Invalid?
   |            |
   |            v
   |      Print invalid message
   |
   v
Check availability
   |
   +------> Already booked?
   |             |
   |             v
   |      Print "Room not available"
   |
   v
Book room
   |
   +--> Set availability = 0
   |
   +--> Calculate total cost
   |
   +--> Increase booking count
   |
   +--> Add revenue
   |
   +--> Print confirmation
   |
   v
Repeat booking loop
   |
   v
Print total booked rooms
   |
   v
Print total revenue
   |
   v
END
'''

# Step 1: Create 2D list
# [room_type, price_per_night, is_available]

rooms = [

    ["Standard", 5000, 1],
    ["Deluxe", 8000, 1],
    ["Suite", 15000, 1],
    ["Family", 10000, 1],
    ["Executive", 20000, 1]

]


# Variable to count total booked rooms
total_booked = 0


# Variable to store total revenue
total_revenue = 0

#Print heading
print("========================================")
print("HOTEL ROOM AVAILABILITY")
print("========================================")

print("No. | Type | Price/Night | Status")

print("----------------------------------------")


# ----------------------------------------
# WHILE LOOP TO DISPLAY ROOMS
# ----------------------------------------

i = 0

while i < len(rooms):

    # Get room information using indexing
    room_type = rooms[i][0]

    room_price = rooms[i][1]

    room_available = rooms[i][2]


    # Check availability
    if room_available == 1:

        status = "Available"

    else:

        status = "Booked"


    # Print room details
    print(
        i + 1,
        "|",
        room_type,
        "|",
        room_price,
        "|",
        status
    )


    # Move to next room
    i += 1


# BOOKING LOOP

while True:

    # Ask user for room number
    room_number = int(input("Enter room number to book (0 to exit): "))


    # Exit condition
    if room_number == 0:

        break


    # Convert room number to index
    index = room_number - 1


    # Check valid room number
    if index >= 0 and index < len(rooms):


        # Check availability
        if rooms[index][2] == 0:

            print("Room not available.")


        else:

            # Update availability
            rooms[index][2] = 0


            # Get room type
            room_type = rooms[index][0]


            # Get price per night
            room_price = rooms[index][1]


            # Calculate total cost for 3 nights
            total_cost = room_price * 3


            # Increase booked count
            total_booked = total_booked + 1


            # Add revenue
            total_revenue = total_revenue + total_cost


            # Print confirmation
            print(
                "Booking confirmed!",
                room_type,
                "room for 3 nights."
            )

            print("Total cost:", total_cost, "yen")


    else:

        print("Invalid room number.")


print("Total rooms booked :", total_booked)

print("Total revenue :", total_revenue, "yen")