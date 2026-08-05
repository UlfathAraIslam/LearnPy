def passing_students(scores_dict, passing_mark=40):
    passed = filter(lambda item: item[1] >= passing_mark, scores_dict.items())
    return sorted(name for name,score in passed)

print(passing_students({"Aisha": 55, "Rafi": 30, "Nadia": 40, "Tanvir": 25}))