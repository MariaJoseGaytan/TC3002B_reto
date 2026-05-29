class Book:
    def __init__(self, title, author, price):
                                                       
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
                                  
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price}")

    def update_price(self, new_price):
                                      
        self.price = new_price

def add_book(books, title, author, price):
                                
    book = Book(title, author, price)
    books.append(book)

def update_book_price(books, title, new_price):
                                         
    for book in books:
        if book.title == title:
            book.update_price(new_price)

def list_books(books):
                    
    for book in books:
        book.display_info()

def main():
                                            
    books = []
    add_book(books, "War and Peace", "Leo Tolstoy", 12.99)
    add_book(books, "The Hobbit", "J.R.R. Tolkien", 9.99)
    
    print("Books available before price update:")
    list_books(books)
    
    update_book_price(books, "The Hobbit", 7.99)
    
    print("\nBooks available after price update:")
    list_books(books)

if __name__ == "__main__":
    main()
