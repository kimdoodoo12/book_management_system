# main.py
from book import Book
import storage
import ui

def main():
    books = storage.load_books()
    ui.show_books(books)

    title, author = ui.get_book_info()
    new_book = Book(title, author)
    books.append(new_book)

    storage.save_books(books)

if __name__ == "__main__":
    main()