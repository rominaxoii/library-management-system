class Book:
    def __init__(self , title , author , year , status="available"):
        self.title = title
        self.author = author
        self.year = year 
        self.status = status

    def borrow(self):
        if self.status == "available" :
            self.status = "borrowed"
        else :
            print(f"Sorry! The book is not available.")
    
    def return_book(self):
        if self.status == "borrowed" :
            self.status = "available"
            print("The book returned!")
        else :
            print("The book wasn't borrowed!")
        
    def is_available(self):
        if self.status == "available":
            print(f"The book is available!")
        else :
            print(f"Sorry , The book is not available!")

    def __str__(self):
        return f"Title : {self.title} , Author : {self.author} , Year : {self.year} , Status : {self.status}"
    
class Library:
    def __init__(self , max_size):
        self.books = []
        self.borrowed_books = []
        self.max_size = max_size

    def add_book(self , title, author, year):
        if len(self.books) + len(self.borrowed_books) < self.max_size :
            b1 = Book(title , author , year)
            self.books.append(b1)
        else :
            print("Sorry, We're at full capacity right now!")

    def find_book(self , title):
        for book in self.books:
            if book.title == title:
                return book
        return None        

    def borrow_book(self , title):
        if self.find_book(title):
            found_book = self.find_book(title)
            found_book.borrow()
            self.books.remove(found_book)
            self.borrowed_books.append(found_book)
        else :
            print("The book wasn't found!")
        
    def return_book(self , title):
        found_book = None
        for book in self.borrowed_books:
            if book.title == title:
                found_book = book
                found_book.return_book()
        if found_book == None :
            print("The book wasn't borrowed!")
        else :
            self.borrowed_books.remove(found_book)
            self.books.append(found_book)

    def show_books(self):
        for book in self.books:
            print(book)
            print("-"*50)


    def show_borrowed(self):
        for book in self.borrowed_books:
            print(book)
            print("-"*50)

    def get_report(self):
        print("="*8 + "Library Report" + "="*8)
        print(f"Available books : {len(self.books)}")
        print(f"Borrowed books : {len(self.borrowed_books)}")
        print(f"Remaining capacity : {self.max_size - len(self.books) - len(self.borrowed_books)}")
l = Library(20)

while True:
    print("\n1. Add Book")
    print("2. Show Available Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show Borrowed Books")
    print("6. Show Report")
    print("7. Exit")

    choice = input(" Enter Your choice: ")

    if choice == "1" :
        title = input("title : ")
        author = input("author : ")
        year = input("year : ")
        l.add_book(title , author , year)

    elif choice == "2" :
        l.show_books()

    elif choice == "3" :
        title = input("title : ")
        l.borrow_book(title)

    elif choice == "4" :
        title = input("title : ")
        l.return_book(title)
    
    elif choice == "5" :
        l.show_borrowed()

    elif choice == "6" :
        l.get_report()

    elif choice == "7":
        break



        