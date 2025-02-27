from datetime import datetime, timedelta

class LMS:
    def __init__(self):
        self.overdue_books={}
        self.borrowing_history={}
        self.borrowed_books={}
        self.books = {
            "Mathematics": ("Jayesh", 5),
            "Physics": ("Milan", 7),
            "Chemistry": ("Sanket", 6),
            "Biology": ("Mehul", 4),
            "Computer Science": ("Mandip", 8),
            "Python Programming": ("Bhargav", 3),
            "English Literature": ("Vishal", 2),
            "History": ("Akash", 5),
            "Geography": ("Sujal", 6),
            "Economics": ("Prince", 4)
        }


    def add_book(self):
        bookname = input("Enter book name:")
        author = input("Enter author name:")
        quantity =int(input("Enter quantity of this book:"))
        self.books[bookname] = (author,quantity)
        print(self.books)

    def remove_book(self):
        bookname = input("Enter book name:")
        self.books.pop(bookname)

    def update_book_info(self):
        bookname = input("Enter book name that you want to update:")
        if bookname in self.books.keys():
            author = input("Author Name:")
            quantity = input("Enter quantity of book:")
            self.books[bookname] = (author,quantity)
        else:
            print("Book not found!")

    def display_available_book(self):
        lst=[]
        for bookname in self.books.keys():
            lst.append(bookname)
        print(f'Available book:{lst}')

class user(LMS):
    def borrow_book(self):
        bookname = input("Enter book name:")
        if bookname not in self.books.keys():
            print("Currently this book is not available!")
            return
        else:
            username = input("Enter your name:")
            if username not in self.borrowed_books.keys():
                brrow_date = datetime.today()
                duedate = brrow_date + timedelta(days=30)
                self.borrowed_books[username] = {bookname:(brrow_date.date(),duedate.date())}
                author,quantity = self.books[bookname]
                self.books[bookname] = (author,quantity-1)
                self.borrowing_history[username] = {bookname:("Borrowed!",brrow_date.strftime("%d/%m/%y"))}
                print(self.borrowed_books)
                print(self.books)
            else:
                brrow_date = datetime.today()
                duedate = brrow_date + timedelta(days=30)
                dict = self.borrowed_books[username]
                history = self.borrowing_history[username]
                if len(dict)<=2:
                    dict[bookname] = (brrow_date.date(),duedate.date())
                    self.borrowed_books[username] = dict
                    history[bookname] = ("Borrowed!",brrow_date.strftime("%d/%m/%y"))
                    self.borrowing_history[username] = history
                    author, quantity = self.books[bookname]
                    self.books[bookname] = (author, quantity-1)
                else:
                    print("you can borrow only 3 book at a time!")

    def return_book(self):
        username = input("Enter your name:")
        if username not in self.borrowed_books.keys():
            print("You don't have any book to return!")
        else:
            bookname = input("Enter book name:")
            dict = self.borrowed_books[username]
            if bookname not in dict.keys():
                print("You are trying to return book that never borrowed!")
            else:
                issue_date = dict[bookname][0]
                return_date = datetime.today()+timedelta(days=30)
                if (return_date.date() - issue_date).days >= 14:
                    print("You have to pay penalty..")
                else:
                    history = self.borrowing_history[username]
                    history[bookname] = ("Return!",return_date.strftime("%d/%m/%y"))
                    self.borrowing_history[username] = history
                    dict.pop(bookname)
                    self.borrowed_books = dict
                    author, quantity = self.books[bookname]
                    self.books[bookname] = (author, quantity + 1)
                    print("return successfully")


    def show_borrowing_history(self):
        print(self.borrowing_history)

    def show_overdue_books(self):
        for username,borrowedbook in self.borrowed_books.items():
            print(f"{username}:{borrowedbook}")
            userdata = self.borrowed_books[username]
            for bookname,bookdate in userdata.items():
                current_date = datetime.today()+timedelta(days=30)
                if (current_date.date() - bookdate[0]).days > 14:
                    if username not in self.overdue_books.keys():
                        self.overdue_books[username] = {bookname:(bookdate[0].strftime("%d/%m/%y"),bookdate[1].strftime("%d/%m/%y"))}
                    else:
                        data = self.overdue_books[username]
                        data[bookname] = (bookdate[0].strftime("%d/%m/%y"),bookdate[1].strftime("%d/%m/%y"))
                        self.overdue_books[username] =data
        print(self.overdue_books)


def assigntask():
    library = LMS()
    user1 = user()
    while True:
        print("Choice:")
        print("1.Add books to the library.")
        print("2.Remove books from the library.")
        print("3.Update book information.")
        print("4.Display available books.")
        print("5.Borrow book.")
        print("6.Return book.")
        print("7.Show borrowing history.")
        print("8.Show overdue books.")
        print("9.Exit")

        try:
            choice = int(input("Enter task choice that you want to perform:"))
            match choice:
                case 1:
                    user1.add_book()
                case 2:
                    library.remove_book()
                case 3:
                    library.update_book_info()
                case 4:
                    library.display_available_book()
                case 5:
                    user1.borrow_book()
                case 6:
                    user1.return_book()
                case 7:
                    user1.show_borrowing_history()
                case 8:
                    user1.show_overdue_books()
                case _:
                    print("Enter valid choice!")
        except Exception as e:
            print(e)

assigntask()



