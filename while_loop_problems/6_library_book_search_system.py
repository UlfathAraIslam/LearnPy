#6
'''
-books = ["Python Crash Course","Harry Potter","SWE","Friends","Family"]
-i = 0
-while true:
-user search for books- input. lower()
-search --exit-> break
-otherwise , if search book available in list--book found
-not available --book not available
-counter increment
-loop end
-print total searches with len(search)
'''
books = [
    "Python Crash Course",
    "Happy",
    "SWE",
    "Friends",
    "Family"
]

total_searches = 0
index = 0

while True:

    search = input("Enter book title (or 'exit' to quit): ").lower()

    if search == "exit":
        break
    total_searches += 1
    while index < len(books):

        if search == books[index].lower():
            print("Book found!")
            break

        index += 1

    else:
        print("Book not available.")

print("Total searches made:", total_searches)