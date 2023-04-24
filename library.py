class Book:
    def __init__ (self, title, author, publisher, year_of_publication, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year_of_publication = year_of_publication
        self.isnb = isbn

    def get_info(self):

        return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, \
             Year of Publication {self.year_of_publication}, ISNB: {self.isnb}"
        
class Library:

    library = []

    def __init__ (self, name, address, list_of_books):
        self.name = name
        self.address = address
        self.list_of_books = list_of_books


    def add_book (self, book):
        self.list_of_books.append(book)
        

    def remove_book (self, book):
        self.list_of_books.remove(book)

    def search_by_title (self, title):
        found_books = []
        for book in self.list_of_books:
            if book.title == title:
                found_books.append(book)
        if found_books:
            return found_books
        else: print ("Book in not in the library")


    def search_by_author (self, author):
        found_books = []
        for book in self.list_of_books:
            if book.author == author:
                found_books.append(book)
        if found_books:
            return found_books
        else: print ("Book in not in the library")

    def search_by_publisher (self, publisher):
        found_books = []
        for book in self.list_of_books:
            if book.publisher == publisher:
                found_books.append(book)
        if found_books:
            return found_books
        else: print ("Book is not in the library")
            

    def search_by_year (self, year_of_publication):
        found_books = []
        for book in self.list_of_books:
            if book.year_of_publication == year_of_publication:
                found_books.append(book)
        if found_books:
            return found_books
        else: print ("book in not in the library")


    def search_by_isbn (self, isbn):
        found_books = []
        for book in self.list_of_books:
            if book.isbn == isbn:
                found_books.append(book)
        if found_books:
            return found_books
        else: print ("Book in not in the library")

martyno_mazvydo_library = Library()

def append_book(martyno_mazvydo_library: Library) -> None:
    title = input("Iveskite knygo pavadinima: ")
    author = input ("Enter book author: ")
    publisher = input ("Enter book publishet: ")
    year_of_publication = int(input("Enter book year of publication"))
    isnb = input("Enter books ISNB: ")

    book_info = Book(title, author, publisher, year_of_publication, isnb)
    martyno_mazvydo_library.add_book(book_info)

def snatch_book(martyno_mazvydo_library: Library) -> None:
    remove_parameter = int(input( "By what parameter you would like to remove your book : \n"
                                    "1 - by title: \n"
                                    "2 - by author: \n" 
                                    "3 - by publisher: \n"
                                    "4 - by year of publication \n"
                                    "5 - by ISNB\n"))


    if remove_parameter == 1: 
        book_title = input("Please enter book's title: ")
        for book in martyno_mazvydo_library.library:
            if book.title == book_title:
                martyno_mazvydo_library.library.remove(book)
                print(f"Book {book_title} is removed")
                return
        print("Book is not present in the library")

    
    elif remove_parameter == 2:
        book_author = input("Please enter your book author")
        for book in martyno_mazvydo_library.library:
            if book.author == book_author:
                martyno_mazvydo_library.library.remove(book)
                print (f"Book {book_author} is removed")
                return
        print("Book is not in the library")

    elif remove_parameter == 3:
        book_publisher = input("Please enter your book publisher: ")
        for book in martyno_mazvydo_library.library:
            if book.publisher ==  book_publisher:
                martyno_mazvydo_library.library.remove(book)
                print (f"Book {book_publisher} is removed")
                return
            else: print("Book is not in the library")

    elif remove_parameter == 4:
        book_year = input("Please enter book's year of release")
        for book in martyno_mazvydo_library.library:
            if book.year_of_publication == book_publisher:
                martyno_mazvydo_library.library.remove(book)
                print (f"Book {book_year} is removed")
                return
            else: print("Book is not in the library")

    elif remove_parameter == 5:
        book_isnb = input("Please enter your book author")
        for book in martyno_mazvydo_library.library:
            if book.isnb == book_isnb:
                martyno_mazvydo_library.library.remove(book)
                print ({f"Book {book_author} is removed"})
                return
            else: print("Book is not in the library")


def search_book ():
    search_parameter = int(input("Please choose paramater by whitch you would like to search your book:: \n"
                                    "1 - by title: \n"
                                    "2 - by author: \n" 
                                    "3 - by publisher: \n"
                                    "4 - by year of publication \n"
                                    "5 - by ISNB\n"))

    if search_parameter == 1:
        book_title = input("Please enter your book title: ")
        for book in martyno_mazvydo_library.library:
         if book.title == book_title:
            print (f"Here is the information of your book: ", book.get_info )
         else: print("Book is not in the library")


    if search_parameter == 2:
        book_author = input("Please enter your book author: ")
        if book_author in martyno_mazvydo_library(book(author)):
            martyno_mazvydo_library.remove_book(author)
            print ("Here is the information of your book: ",  book.get_info )
        else: print("Book is not in the library")


    if search_parameter == 3:
        book_publisher = input("Please enter your book publisher: ")
        if book_publisher in martyno_mazvydo_library(book(publisher)):
            martyno_mazvydo_library.remove_book(author)
            print (f"Here is the information of your book: ", book.get_info )
        else: print("Book is not in the library")

    if search_parameter == 4:
        book_year = input("Please enter your book's  year of publication: ")
        if book_year in martyno_mazvydo_library(book(year_of_publication)):
            martyno_mazvydo_library.remove_book(year)
            print (f"Here is the information of your book: ", book.get_info )
        else: print("Book is not in the library")

    if search_parameter == 4:
        book_year = input("Please enter your book's  year of publication: ")
        if book_year in martyno_mazvydo_library(book(year_of_publication)):
            martyno_mazvydo_library.remove_book(year)
            print (f"Here is the information of your book: ", book.get_info )
        else: print("Book is not in the library")

