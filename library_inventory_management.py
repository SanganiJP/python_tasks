from datetime import datetime, timedelta
from time import strftime

books = {}
borrowedbooks = {}
mybooks = {}
dates = {}

class libInventoryManagement():
    def __init__(self,books,borrowedbooks,mybooks):
        self.books = books

    def addbook(self,bookname,author,quantity):
        books[bookname] = (author,quantity)
        print(books)
        return books

    def removebook(self,bookname):
        books.pop(bookname)
        print(books)
        return books

    def updatebook(self,bookname,author,quantity):
        books[bookname] = (author,quantity)
        print(books)
        return books

    def displaybook(self):
        print("Available Books:",self.books)


class userSystem(libInventoryManagement):
    def __init__(self,books,borrowedbooks,mybooks):
        self.books = books
        self.borrowedbooks = borrowedbooks
        self.mybooks = mybooks
        # super().__init__(books=books,borrowedbooks=borrowedbooks,mybooks=mybooks)
            # self.books = books
            # self.borrowedbooks = borrowedbooks
            # self.mybooks = mybooks

    def borrowBook(self,name,mybooks,bookname):
        if bookname not in books.keys():
            print("Currently this book is out of stock!")
        else:
            if len(mybooks)<=3:
                brrow_date = datetime.today()
                duedate = brrow_date + timedelta(days=14)
                day = duedate-brrow_date
                print(day)
                dates[bookname] = (brrow_date,duedate)
                mybooks[bookname] = (brrow_date.strftime("%d/%m/%y"),duedate.strftime("%d/%m/%y"))
                borrowedbooks[name] = mybooks
                libdata = books[bookname]
                authorname = libdata[0]
                bookquantity = libdata[1]-1
                super().updatebook(bookname=bookname,author=authorname,quantity=bookquantity)
                # books[bookname] = (authorname,bookquantity-1)

                print(borrowedbooks)
            else:
                print("You can only borrow up to 3 books at a time.")
        return borrowedbooks

    def returnBook(self,name,dates,bookname):
        dates = dates[bookname]
        issue_date = dates[0]
        return_date = datetime.today()
        if (return_date-issue_date).days > 14:
            print("You have to penalty..")
        else:
            mybooks.pop(bookname)
            libdata = books[bookname]
            authorname = libdata[0]
            bookquantity = libdata[1]+1
            super().updatebook(bookname=bookname, author=authorname, quantity=bookquantity)
            borrowedbooks[name] = mybooks
            print("book return successfully!")

l1 = libInventoryManagement(books,borrowedbooks,mybooks)
l1.addbook(bookname="eng",author="Milan",quantity=20)
l1.addbook(bookname="mahabharata",author="Vyasa",quantity=5)
u1 = userSystem(books,borrowedbooks,mybooks)
u1.borrowBook(name="jayesh",bookname="eng",mybooks=mybooks)
l1.displaybook()
u1.returnBook(name="jayesh",bookname="eng",dates=dates)


