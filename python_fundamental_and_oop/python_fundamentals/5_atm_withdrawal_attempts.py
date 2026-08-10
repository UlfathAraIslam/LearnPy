correct_pin = 1234
attempts = 0

while attempts < 3:
    pin = int(input("Enter PIN: "))

    if pin == correct_pin:
        print("Access granted")
        break
    attempts += 1
else:
    print("Card blocked")
