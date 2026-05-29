class Book:
    def __init__(self, title, author, price):
                                                       
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
                                  
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price}")

def add_book(books, title, author, price):
                                      
    book = Book(title, author, price)
    books.append(book)

def list_books(books):
                                 
    for book in books:
        book.display_info()

def main():
                                                   
    books = []
    add_book(books, "The Catcher in the Rye", "J.D. Salinger", 10.99)
    add_book(books, "To Kill a Mockingbird", "Harper Lee", 7.99)
    
    print("Books available in the store:")
    list_books(books)

if __name__ == "__main__":
    main()
