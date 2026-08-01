def rating_label(score):
    if 1 <=score<=2:
        return "Beginner"
    elif score == 3:
        return "Intermediate"
    elif score == 4:
        return "Advanced"
    elif score == 5:
        return "Expert"
    else:
        return "Invalid"
print(rating_label(4))
print(rating_label(1))
print(rating_label(9))