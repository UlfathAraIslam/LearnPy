#8
'''
-take an empty array for all scores = []
-region_a = [88, 74, 95, 61]
-region_b = [79, 91, 85, 70].
-all scores.extend(region_a,region_b) to merge
-all scores.sort(reverse= True) for descending sort
-print all scores
-slice[:3] for top 3 scores
print top finalists
-checking highest score
-If the highest score is above 90, print 'A score above 90 made it to the podium!
-else print 'No score above 90 this season'.
'''
region_a = [88, 74, 95, 61]
region_b = [79, 91, 85, 70]
region_a.extend(region_b)
region_a.sort(reverse=True)

print("All scores:",region_a)
print("Top 3 finalists:",region_a[:3])
if region_a[0]>90:
    print("A score above 90 made it to the podium!")
else:
    print("No score above 90 this season")