from datetime import date, timedelta

class Book:
    
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.user = None
        self.loan_date = None


    def __str__(self):
        if self.user:
            formatted_date = self.loan_date.strftime("%d-%B-%Y")
            return f"{self.name} - {self.author}. Loaned by:{self.user} - on:{formatted_date}"
        else:
            return f"{self.name} - {self.author}. BOOK IS FREE"
        
    def loan_book(self, user):
        self.user = user
        self.loan_date = date.today()
        print("you should return in ",self.loan_date + timedelta(days=10))


    def return_book(self):
        date_of_return = date.today()
        if (date_of_return > self.loan_date + timedelta(days=10)):
            print("50 shekel FINE!!!")
        self.user = None
        self.loan_date = None