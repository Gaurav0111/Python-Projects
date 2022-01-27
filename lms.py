from operator import truediv


class library:
    def __init__(self,listofbooks):
        self.books = listofbooks

    def displayavailablebooks(self):
        print("The books present in the library are")
        for book in self.books:
            print(" *" + book)

    def borrowbook(self , bookname):
        if bookname in self.books:
            print(f"You haved issued the book {bookname}")
            print("Thank You!")
            self.books.remove(bookname)
            return True
        else :
            print("This book is either not available or the Book have already been issued to someone else")
            return False

    def returnbook(self,bookname):
        self.books.append(bookname)
        print("Book has been returned")
       

class student:

    def requestbook(self):
        self.book = input("Enter the name of the book you want to borrow : ")
        return self.book

    def returnbook(self):
        self.book = input("Enter the name of the book you want to return : ")
        return self.book

if __name__=="__main__":
    centralibrary = library(["Algo" , "Software" , "Computer Network" , "Advance Java " , " Django"])
    student = student()
    while (True):
        welcomemsg = '''\n  ____________Welcome to central library________________
        Please choose an option:
        1. List all the books
        2. Request a book 
        3. Add or Return a book
        4. Exit the Library
        '''
        print(welcomemsg)
        a = int(input("Enter a choice : "))
        if a == 1:
            centralibrary.displayavailablebooks()
        elif a==2:
            centralibrary.borrowbook(student.requestbook())
        elif a==3:
            centralibrary.returnbook(student.returnbook())
        elif a==4:
            print("Thanks for choosing Library!. Have a great day")
            exit()
        else:
            print("Invalid choise! ")
