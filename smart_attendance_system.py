attendance= input("Enter attendance:")
assignment_submission_status = input("Assignment submitted?").lower()

if attendance.isdigit():
    attendance = int(attendance)
    if attendance >= 75 and assignment_submission_status == "yes":
        print ("Eligible for final exam")
    elif attendance <75:
        print("Not eligible (low attendance)")
    elif assignment_submission_status == "no":
        print("Not eligible (missing assignment)")
else:
    print("Enter valid number")