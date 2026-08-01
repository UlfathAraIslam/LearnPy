def attendance_status(attended, total):
        return "Eligible" if attended / total >= 0.75 else "Not Eligible"
print(attendance_status(20, 26))
print(attendance_status(15, 26))