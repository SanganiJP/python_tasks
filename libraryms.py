from datetime import datetime, timedelta


def addbook(books):
    try:
        booktitle = input("Enter book title:")
        if booktitle not in books.keys():
            author = input("Enter name of author:")
            quantity = int(input("Enter quantity of this book:"))
            books[booktitle] = (author, quantity)
            print("Book added successfully!")
        else:
            print("You are trying to add existing book!")
        managertask()
    except Exception as e:
        print(e)


def removebook(books):
    try:
        booktitle = input("Enter book title that you want to remove:")
        if booktitle in books.keys():
            books.pop(booktitle)
            print("Removed Successfully")
        else:
            print("you are trying remove a non-existing book!")
            print()
        managertask()
    except Exception as e:
        print(e)

def updateinfo(books):
    try:
        bookName = input("Enter book name that you want to update:")
        if bookName in books.keys():
            authorName = input("Author Name:")
            quantity = input("Enter quantity of book:")
            books[bookName] = (authorName,quantity)
        else:
            print("Book not found!")
        managertask()
    except Exception as e:
        print(e)

def displaybook(books):
    try:
        print(f'Available Books:')
        print(books)
        for book in books.keys():
            print(f'{book}')
        managertask()
    except Exception as e:
        print(e)

def searchbook(books):
    try:
        bookname = input("Enter book name you want to search:")
        if bookname in books.keys():
            Bookname = bookname
            info = books.get(bookname)
            author = info[0]
            quantity = info[1]
            print(f'Book Details: Name of Book:{Bookname} Author:{author} Available Quantity:{quantity}')
        else:
            print("Sorry! Books not found!")
        managertask()
    except Exception as e:
        print(e)

""" 
User task functions
"""
def borrow_books(books,borrowedbook,mybooks):
    bookname = input("Enter book name that you want to borrow:")
    if bookname not in books.keys():
        print("Currently this book is not available!")
        usertask()
    else:
        if (len(mybooks) <= 1) :
            username = input("Enter your name:")
            brrow_date = datetime.today()
            duedate = brrow_date + timedelta(days=30)
            mybooks[bookname] = (brrow_date.strftime("%d/%m/%y"), duedate.strftime("%d/%m/%y"))
            borrowedbook[username] = mybooks
            bookdata = books[bookname]
            a = bookdata[0]
            q = bookdata[1] - 1
            books[bookname] = (a, q)
            usertask()
        else:
            print("Users can only borrow a maximum of 2 books at a time.")
            usertask()
    return borrowedbook

def return_books(books,borrowedbook,mybooks):
    name = input("Enter your name:")
    if name in borrowedbook.keys():
        bookname = input("Enter book name you want to return:")
        if bookname in mybooks.keys():
            bookdata = books[bookname]
            a = bookdata[0]
            q = bookdata[1] + 1
            books[bookname] = (a, q)
            mybooks.pop(bookname)
            print("Book return successfully, Thank You!")
            usertask()
    else:
        print("Returning books not borrowed")
        usertask()


def view_your_books(result):
    username = input("Enter your name:")
    if username in result:
        print(result)
        usertask()
    else:
        print("You don't have any book!")
        usertask()

books={"math":("jayesh",10)}
borrowedbook = {}
mybooks = {}

def checkUser():
    print("Select:")
    print("1.Enter 1 if you are user")
    print("2.Enter 2 if you are admin")
    print("3.Exit")
    userType = int(input("Select your role:"))
    return userType

def takechoice():
    print("Choice:")
    print("1.Add books to the library.")
    print("2.Remove books from the library.")
    print("3.Update book information.")
    print("4.Display available books.")
    print("5.Search for books by title.")
    print("6.Exit")
    choice = int(input("Enter task choice that you want to perform:"))
    return choice

def takeuserchoice():
    print("Select:")
    print("1.Borrow books")
    print("2.Return books")
    print("3.View your books")
    print("4.Exit")
    choice = int(input("Enter task choice that you want to perform:"))
    return choice

def assignTask():
    userType = checkUser()
    if userType == 1:
        usertask()
    elif userType == 2:
        managertask()
    else:
        return

def managertask() :
    try:
        choice = takechoice()
        if choice == 1:
            addbook(books)
        elif choice == 2:
            removebook(books)
        elif choice == 3:
            updateinfo(books)
        elif choice == 4:
            displaybook(books)
        elif choice == 5:
            searchbook(books)
        elif choice == 6:
           assignTask()
        else:
            print("Enter valid choice")
    except Exception as e:
        print(e)

def usertask():
    try:
        choice = takeuserchoice()
        if choice == 1:
            borrow_books(books,borrowedbook,mybooks)
        elif choice == 2:
            return_books(books,borrowedbook,mybooks)
        elif choice == 3:
            view_your_books(borrowedbook)
        elif choice == 4:
           assignTask()
        else:
            print("Enter valid choice")
    except Exception as e:
        print(e)

assignTask()