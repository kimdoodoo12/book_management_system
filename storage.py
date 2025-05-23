# storage.py
import json
from book import Book
def save_books(books, filename='books.json'):
    with open(filename, 'w') as f:
        json.dump([book.__dict__ for book in books], f)

def load_books(filename='books.json'):
    try:
        with open(filename, 'r') as f:
            books = json.load(f)
            return [Book(**b) for b in books]
    except FileNotFoundError:
        return []