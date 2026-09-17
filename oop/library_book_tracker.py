class Book:
    def __init__(self,book_id,title,author,available=True):
        self.title = title
        self.author = author
        self.available = available
    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available}"
class Library:
    def __init__(self):
        self.books = []
        self.next_id = 1
    
