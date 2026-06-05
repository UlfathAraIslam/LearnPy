# Train names

trains = ["Nozomi", "Hikari", "Kodama", "Sakura"]

# Seat class names

seat_classes = ["Green","Reserved","Unreserved",
"Standing","Disabled"
]

# 2D list
# seats[train][seat_class]

seats = [

    [12, 45, 0, 0, 3],   # Nozomi
    [0, 10, 22, 15, 2],  # Hikari
    [5, 0, 30, 40, 0],   # Kodama
    [8, 20, 18, 0, 5]    # Sakura
]

# Heading

print("========================================")
print("TRAIN SEAT AVAILABILITY")
print("========================================")

# Table heading

print("Train | Green | Reserved | Unreserved | Standing |Disabled")

print("--------------------------------------------------------------------")

# Train index

t = 0

# Print all train seat data

while t < len(trains):

    print(
        f"{trains[t]} | "
        f"{seats[t][0]} | "
        f"{seats[t][1]} | "
        f"{seats[t][2]} | "
        f"{seats[t][3]} | "
        f"{seats[t][4]}"
    )

    t += 1

# User search loop

while True:

    # Input train number

    train_index = int(
        input("Enter train number to check (0-3, or -1 to exit): ")
    )

    # Exit condition

    if train_index == -1:

        print("Goodbye!")
        break

    # Check valid train number

    if train_index >= 0 and train_index < len(trains):

        print(
            f"--- {trains[train_index]} Seat Status ---"
        )

        # Seat class index

        c = 0

        # Loop through seat classes

        while c < len(seat_classes):

            current_seat = seats[train_index][c]

            # Check seat availability

            if current_seat > 0:

                print(
                    f"{seat_classes[c]} : "
                    f"Available ({current_seat} seats)"
                )

            else:

                print(
                    f"{seat_classes[c]} : Full"
                )

            c += 1

    else:

        print("Invalid train number")