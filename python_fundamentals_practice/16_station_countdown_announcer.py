def countdown_announcements(minutes):
    annuncements = []
    for m in range(minutes,-1,-1):
        if m == 0:
            annuncements.append("Departing now!")
        else:
            annuncements.append(f"{m} minutes to departure")
    return annuncements
print (countdown_announcements(3))