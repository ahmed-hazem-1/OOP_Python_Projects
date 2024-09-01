# main.py

from Library import Library

# Initialize Library
alex_library = Library()
Exit_program = False

print("Hello, How can I help you?\n")
while not Exit_program:
    command = input("\n1: List of Members\n"
                    "2: List of Books\n"
                    "3: Add Book\n"
                    "4: Add Member\n"
                    "5: Lend Book\n"
                    "6: Return Book\n"
                    "7: Close The Program\n"
                    "Enter your choice: ")

    if command == '1':
        alex_library.list_members()
    elif command == '2':
        alex_library.list_books()
    elif command == '3':
        alex_library.add_book()
    elif command == '4':
        alex_library.add_member()
    elif command == '5':
        alex_library.lend_book()
    elif command == '6':
        alex_library.return_book()
    elif command == '7':
        Exit_program = True
    else:
        print("Invalid choice.")
