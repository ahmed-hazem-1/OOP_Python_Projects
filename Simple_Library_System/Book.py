# book.py

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")

    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returned(self):
        self.is_borrowed = False
