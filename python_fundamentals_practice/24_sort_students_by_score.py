def sort_students(students):
    ranked = sorted(students,key=lambda s: s["score"],reverse=True)
    return [s["name"] for s in ranked]
print(sort_students([
    {"name": "Aisha", "score": 88},
    {"name": "Rafi", "score": 95},
    {"name": "Tanvir", "score": 75}
]))

'''
sorted(
    data,
    key=lambda item: item["something"],
    reverse=True
)
This pattern appears everywhere:

leaderboard ranking
product price sorting
employee salary ranking
student grades
website search results.
'''
