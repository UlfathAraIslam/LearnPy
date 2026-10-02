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
