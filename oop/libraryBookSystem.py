class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f'"{self.title}" is already borrowed.')
            return
        self.is_borrowed = True
        print(f'"{self.title}" borrowed successfully.')

    def return_book(self):
        if not self.is_borrowed:
            print(f'"{self.title}" was not borrowed.')
            return
        self.is_borrowed = False
        print(f'"{self.title}" returned successfully.')
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for b in self.books:
            if b.title == title:
                return b
        return None
def main():
    library = Library()
    count = int(input("How many books do you want to add? "))
    for _ in range(count):
        title = input("Book title: ")
        author = input("Author: ")
        library.add_book(Book(title, author))

    while True:
        action = input("Action (borrow/return/done): ")
        if action == "done":
            break
        title = input("Enter book title: ")
        book = library.find_book(title)
        if book is None:
            print(f'"{title}" not found in library.')
            continue
        if action == "borrow":
            book.borrow()
        elif action == "return":
            book.return_book()
        else:
            print("Unknown action, skipping.")


if __name__ == "__main__":
    main()