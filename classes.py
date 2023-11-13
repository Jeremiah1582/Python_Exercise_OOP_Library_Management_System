
class Book:
    def __init__(self, title, author, refNum):
        self.title = title
        self.author = author
        self.refNum = refNum
        self.available = True

class Patron:
    def __init__(self, name,email, card_number):
        self.name = name
        self.email=email
        self.card_number = card_number
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)

    def register_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self, patron, book):
        if book.available:
            book.available = False
            patron.borrowed_books.append(book)
            self.transactions.append(f"{patron.name} borrowed '{book.title}'.")
        else:
            print("Sorry, this book is not available.")

    def return_book(self, patron, book):
        if book in patron.borrowed_books:
            book.available = True
            patron.borrowed_books.remove(book)
            self.transactions.append(f"{patron.name} returned '{book.title}'.")
        else:
            print("You didn't borrow this book.")

    def check_book_availability(self, book):
        return book.available

    def display_books(self):
        for book in self.books:
            status = "Available" if book.available else "Not Available"
            print(f"{book.title} by {book.author} ({book.refNum}) - {status}")

    def display_patrons(self):
        for patron in self.patrons:
            print(f"{patron.name}\nEmail: {patron.email}\nCard No: {patron.card_number}")

    def display_transactions(self):
        for transaction in self.transactions:
            print(transaction)
