def log_attendance(file_path, student_name):
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"{student_name} - present\n")
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return len(lines)

print (log_attendance("attendance.txt", "Rafi"))
print (log_attendance("attendance.txt", "Nadia"))
print (log_attendance("attendance.txt", "Tanvir"))