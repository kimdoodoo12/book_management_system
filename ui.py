# ui.py
def show_books(books):
    for book in books:
        print(f"{book.title} by {book.author}")

def get_book_info():
    title = input("Title: ")
    author = input("Author: ")
    return title, author