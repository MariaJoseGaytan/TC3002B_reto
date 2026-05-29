class Book:
    def __init__(self, title, author, price, genre):
                                                              
        self.title = title
        self.author = author
        self.price = price
        self.genre = genre

    def display_info(self):
                                                  
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price}, Genre: {self.genre}")

def add_book(books, title, author, price, genre):
                                                       
    book = Book(title, author, price, genre)
    books.append(book)

def list_books(books):
                                 
    for book in books:
        book.display_info()

def main():
                                                   
    books = []
    add_book(books, "The Alchemist", "Paulo Coelho", 10.49, "Fiction")
    add_book(books, "Sapiens", "Yuval Noah Harari", 14.99, "Non-fiction")
    
    print("Books available in the store with genre info:")
    list_books(books)

if __name__ == "__main__":
    main()
