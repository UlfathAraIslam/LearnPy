#6
'''
-start with Given ratings = [3.8, 4.5, 2.9, 4.8, 4.1].
-print the highest use max()
-print the lowest rating use min()
-sort ratings highest to lowest (ratings, reverse=True) — do not modify original list.
-checking top rating
-if rating is >= 4.5, print 'Top restaurant qualifies for Featured badge!
-else print 'No featured badge this week
'''

ratings = [3.8, 4.5, 2.9, 4.8, 4.1]
highest_ratings = max(ratings)
lowest_ratings = min(ratings)
print(f"Highest: {highest_ratings} | Lowest: {lowest_ratings}")
ranked = sorted(ratings,reverse=True)
print("Ranked:",ranked)

top_rating = ranked[0]

if top_rating >= 4.5:
    print("Top restaurant qualifies for Featured badge!")
else:
    print("No featured badge this week")