import csv
#Main classes for library including Book, Patron, Transaction, and Library class along with user interface
#Book class used to create book objects and display details
class Book:
    def __init__(self, title, author, isbn, quantity):
        self.title = title
        self.author = author
        self.isbn = str(isbn)
        self.quantity = quantity

    def display_details(self):
        return [self.title, self.author, self.isbn, self.quantity]
class Patron:
    def __init__(self, name, patron_id, contact_info):
        self.name = name
        self.patron_id = patron_id
        self.contact_info = contact_info
    def display_details(self):
            print("Name: {}, ID: {}, Contact: {}".format(self.name, self.patron_id, self.contact_info))

#Transaction class handles check-in and check-out of books
class Transaction:
    def __init__(self, book, patron):
        self.book = book
        self.patron = patron
        self.checked_out = False

    def check_out(self):
        if self.book.quantity > 0:
            self.book.quantity -= 1
            self.checked_out = True
            print("Book '{}' checked out to '{}'".format(self.book.title, self.patron.name))
        else:
            print("Sorry, '{}' is out of stock.".format(self.book.title))

    def check_in(self):
        if self.checked_out:
            self.book.quantity += 1
            self.checked_out = False
            print("Book '{}' checked in.".format(self.book.title))
        else:
            print("Book '{}' is not checked out.".format(self.book.title))
#Library class add/removes and updates books and patrons
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print("{} added.".format(book.title))

    def add_patron(self, patron):
        self.patrons.append(patron)
        print("Patron added")

    def update_book(self, isbn, new_quantity):
        for book in self.books:
            if book.isbn == isbn:
                book.quantity = new_quantity
                print("Book quantity updated.")
                return
        print("Book not found.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print("Book removed.")
                return
        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            book.display_details()

    def display_patrons(self):
        if not self.patrons:
            print("No patrons registered.")
            return
        for patron in self.patrons:
            patron.display_details()


#Admin interface
def admin_int(library):
    print("Welcome, Admin!")
    action = input("Would you like to add/remove a book (add/remove) or view patrons (patron)? ")

    if action == "add":
        add_book_int(library)
    elif action == "remove":
        remove_book_int(library)
    elif action == "patron":
        library.display_patrons()
    else:
        print("Please try again.")


#Admin interface for adding a book
def add_book_int(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN of the book: ")
    quantity = int(input("Enter the quantity of the book: "))

    new_book = Book(title, author, isbn, quantity)
    library.add_book(new_book)


#Admin interface for removing a book
def remove_book_int(library):
    isbn = input("Enter the ISBN of the book you want to remove: ")
    library.remove_book(isbn)


def user_int(library):
    print("Welcome")
    catalog = input("Would you like to view all of the books? (y/n) ")
    if catalog == "y":
        export_books_to_csv(library.books)
    action = input("Would you like to check out (check out) or check in (check in) a book? ")

    if action == "check out":
        check_out_int(library)
    elif action == "check in":
        check_in_int(library)
    else:
        print("Please try again.")


# user interface for checking out a book
def check_out_int(library):
    isbn = input("Enter the ISBN of the book you want to check out: ")
    patron_id = int(input("Enter your patron ID: "))

    patron = find_patron_by_id(library, patron_id)
    if patron:
        book = find_book_by_isbn(library, isbn)
        if book:
            transaction = Transaction(book, patron)
            transaction.check_out()
        else:
            print("Book not found.")
    else:
        print("Patron not found.")


#user interface for checking in a book
def check_in_int(library):
    isbn = input("Enter the ISBN of the book you want to check in: ")
    patron_id = int(input("Enter your patron ID: "))

    patron = find_patron_by_id(library, patron_id)
    if patron:
        book = find_book_by_isbn(library, isbn)
        if book:
            transaction = Transaction(book, patron)
            transaction.check_in()
        else:
            print("Book not found.")
    else:
        print("Patron not found.")


#find a patron by ID
def find_patron_by_id(library, patron_id):
    for patron in library.patrons:
        if patron.patron_id == patron_id:
            return patron
    return None


#find a book by ISBN
def find_book_by_isbn(library, isbn):
    for book in library.books:
        if book.isbn == isbn:
            return book
    return None

#exports all library books to csv
def export_books_to_csv(books):
    file_path = 'library_books.csv'
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Author", "ISBN", "Quantity"])
        for book in books:
            writer.writerow(book.display_details())
    print("Library books exported to library_books.csv")

#main function
def main():
    #ceate book objects for library
    library = Library()
    book1 = Book("magic_school_bus", "sum lady", 6534787, 3)
    book2 = Book("the_odyssey", "homer", 4376086, 2)
    book3 = Book("romeo_and_juliet", "shakespeare", 9473832, 1)
    book4 = Book("harry_potter", "j.k. rowling", 567898765, 2)
    book5 = Book("ispy", "jean marzollo", 42762389, 0)
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)

    #create patrons for library
    patron1 = Patron("Alice", 1, "alice@example.com")
    patron2 = Patron("Bob", 2, "bob@example.com")
    patron3 = Patron("Nick", 3, "nick@example.com")
    library.add_patron(patron1)
    library.add_patron(patron2)
    library.add_patron(patron3)

    #user interface for user and admin
    user_or_admin = input("\nAre you a user or an admin? (user/admin) ")
    if user_or_admin == "admin":
        admin_int(library)
    elif user_or_admin == "user":
        user_int(library)
    else:
        print("Please try again.")

#Use of implemetation
if __name__ == "__main__":
    main()

