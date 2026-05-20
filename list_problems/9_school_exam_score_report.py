#9
#*TODO
'''
-start with Given scores = [[85, 90, 78], [92, 88, 95], [70, 75, 80]]
-math scores[0,0]
-math scores[1,0]
-math scores[2,0]
-print math scores using extend or concatenation
-highest score max(score)
-print science score scores[1][1]
'''
scores =[
    [85, 90, 78], #student 1
    [92, 88, 95], #student 2
    [70, 75, 80]  #student 3
]
# math scores (index 0) 
print(f"Maths scores -> Student 1: {scores[0][0]} | Student 2: {scores[1][0]} | Student 3: {scores[2][0]}")

# create a flat list
all_scores = []

all_scores.extend(scores[0])
all_scores.extend(scores[1])
all_scores.extend(scores[2])

# highest score
highest_score = max(all_scores)
print("Highest score in class:", highest_score)

# science score of student 2
print("Student 2's Science score:",scores[1][1])

