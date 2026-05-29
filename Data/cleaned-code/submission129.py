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

def remove_book(books, title):
                                
    books[:] = [book for book in books if book.title != title]

def list_books(books):
                    
    for book in books:
        book.display_info()

def main():
                                                   
    books = []
    add_book(books, "Moby Dick", "Herman Melville", 11.99)
    add_book(books, "Pride and Prejudice", "Jane Austen", 6.99)
    
    print("Books available before removal:")
    list_books(books)
    
    remove_book(books, "Moby Dick")
    
    print("\nBooks available after removal:")
    list_books(books)

if __name__ == "__main__":
    main()
