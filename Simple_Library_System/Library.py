# library.py

from Book import Book
from Member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        title = input("Please enter the book title: ")
        author = input("Please enter the book author: ")
        isbn = input("Please enter the book ISBN: ")
        book = Book(title, author, isbn)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def add_member(self):
        name = input("Please enter the member's name: ")
        member_id = input("Please enter the member ID: ")
        member = Member(name, member_id)
        self.members.append(member)
        print(f"Member '{name}' added to the library.")

    def lend_book(self):
        isbn = input("Please enter the book ISBN to lend: ")
        member_id = input("Please enter the member ID: ")
        book = next((b for b in self.books if b.isbn == isbn), None)
        member = next((m for m in self.members if m.member_id == member_id), None)

        if book is None:
            print("Book not found.")
        elif member is None:
            print("Member not found.")
        elif book.is_borrowed:
            print("Sorry, this book is currently borrowed.")
        else:
            member.borrow_book(book)
            book.mark_as_borrowed()
            print(f"The book '{book.title}' has been lent to {member.name}.")

    def return_book(self):
        isbn = input("Please enter the book ISBN to return: ")
        member_id = input("Please enter the member ID: ")
        book = next((b for b in self.books if b.isbn == isbn), None)
        member = next((m for m in self.members if m.member_id == member_id), None)

        if book is None:
            print("Book not found.")
        elif member is None:
            print("Member not found.")
        elif book not in member.borrowed_books:
            print("This book was not borrowed by this member.")
        else:
            member.return_book(book)
            book.mark_as_returned()
            print(f"The book '{book.title}' has been returned by {member.name}.")

    def list_books(self):
        if self.books:
            for book in self.books:
                book.display_info()
        else:
            print("No books available.")

    def list_members(self):
        if self.members:
            for member in self.members:
                print(f"Name: {member.name}, ID: {member.member_id}")
        else:
            print("No members available.")
