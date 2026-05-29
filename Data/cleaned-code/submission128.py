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

def search_book(books, title):
                                
    for book in books:
        if book.title == title:
            book.display_info()

def list_books(books):
                                 
    for book in books:
        book.display_info()

def main():
                                            
    books = []
    add_book(books, "The Great Gatsby", "F. Scott Fitzgerald", 8.99)
    add_book(books, "1984", "George Orwell", 9.99)
    
    print("Books available in the store:")
    list_books(books)
    
    print("\nSearching for '1984':")
    search_book(books, "1984")

if __name__ == "__main__":
    main()
