#5
'''
-start given a list of headlines ["headlines1","headlines2","headlines3","New Ai Law Passed","Budget Cuts Announced","School Reform Bill"]
-recent variable to keep the last 3 headlines
-print total headlines count and recent count
-access each item by index and apply title()
-Print each recent headline numbered and in title case.
-check total headlines count
-if headlines are fewer than 3 print not enough news yet
'''
headlines = ["headlines1","headlines2","New Ai Law Passed","Budget Cuts Announced","School Reform bill"]
recent= headlines[-3:]
total_headings = len(headlines)
if total_headings<3:
    print("Not enough news yet")

print(f"Total headlines: {total_headings} | Showing: {len(recent)}")
print("1.",recent[0].title())
print("2.",recent[1].title())
print("3.",recent[2].title()) 