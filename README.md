Exercise: Library Management System

# Backstory:
You've been hired to develop a library management system for a local library. The library wants to modernize its operations and improve user experience. You'll be creating a Python program that simulates the library's functionalities.

# Objectives:
Design and implement a Library class to manage books, patrons, and transactions. The program should provide options to borrow and return books, check available books, and more.

# Tasks:

1) Create a Book Class:
- Design a Book class that contains information about a book, such as its 
    >title, 
    >author, 
    >Reference Number,
    >availability status.

2) Create a Patron Class:
- Design a Patron class that represents library patrons. 
- Patrons should have attributes like 
    >name, 
    >email
    >library card number, 
    > and a list of borrowed books.

3) Create a Library Class:
- Implement a Library class that manages books, patrons, and transactions.

4) The Library class should have methods for:
- Adding books to the library.
- Registering new patrons.
- Borrowing books (a patron checks out a book).
- Returning books (a patron returns a book).
- Checking the availability of a book.
- Displaying a list of all books in the library.
- Displaying a list of all registered patrons.
- Displaying a list of all transactions (who borrowed which book and when).

5) User Interface:
- Implement a command-line user interface that allows library staff to interact with the system.
- Provide options to perform the actions mentioned above, and guide the user through the process.

6) Resource Tracking:
Ensure that the Library class keeps track of available books and who has borrowed them.

7) Transaction History:
Record transaction history, so it's possible to view who borrowed or returned a book and when.

# Error Handling: *Good Practice*
Implement error handling to handle scenarios like a patron trying to borrow an unavailable book, returning a book they didn't borrow, or entering invalid book titles or patron card numbers.

# Additional Tips: *Senior*
- Create well-structured classes with clear separation of responsibilities.
- Use appropriate data structures to manage books, patrons, and transactions.
- Consider how to handle edge cases and provide informative error messages when needed.
- Make the user interface intuitive and user-friendly.

# Summary:
This exercise simulates the development of a library management system. It's a practical application of object-oriented programming principles, including class design, methods, data structures, and user interaction. You'll gain experience in building a system that manages resources, tracks transactions, and provides functionality to library staff.