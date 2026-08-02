def find_seat(seating, name):
    row = 0
    while row < len(seating):
        col = 0
        while col < len(seating[row]):
            if seating[row][col] == name:
                return (row, col)
            col += 1
        row += 1
    return None
seating = [
    ["Aisha", "Rafi", None],
    [None, "Tanvir", "Nadia"]
]
print(find_seat(seating, "Nadia"))
