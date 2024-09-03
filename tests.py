from book.models import Book
from user.models import User
from datetime import date, timedelta

def test_check_loan_return():
    # create 2 books and 2 users and loan the books
    book1 = Book("My Book 1","Ran")
    book2 = Book("My Book 22","Chana")
    user1 = User("Raz","054-3332233")
    user2 = User("Inbal","052-3442233")
    book1.loan_book(user1)
    book2.loan_book(user2)
    print("1111", book1)
    print("1111", book2)

    book1.return_book()
    book2.return_book()
    print("2222",book1)
    print("2222",book2)


def test_late_loan():
    # create 1 books and 1 users and loan the books. late return
    book1 = Book("My Book 1","Ran")
    user1 = User("Raz","054-3332233")
    book1.loan_book(user1)
    print("1111", book1)
    book1.loan_date = date.today() - timedelta(days=20)
    book1.return_book()

def test_not_late_loan():
    # create 1 books and 1 users and loan the books. late return
    book1 = Book("My Book 1","Ran")
    user1 = User("Raz","054-3332233")
    book1.loan_book(user1)
    print("1111", book1)
    # book1.loan_date = date.today() - timedelta(days=20)
    book1.return_book()

# test_check_loan_return()
test_not_late_loan()