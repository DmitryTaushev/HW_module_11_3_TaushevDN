import json
import logging


logging.basicConfig(filename='library.log', level=logging.INFO)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Librarian:
    def __init__(self, name):
        self.name = name

class Reader:
    def __init__(self, name):
        self.name = name

class EntityFactory:
    @staticmethod
    def create_book(title, author):
        return Book(title, author)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        logging.info(f'Added book: {book.title}')

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]
        logging.info(f'Removed book: {title}')

    def save_to_file(self, filename):
        with open(filename, 'w',encoding = 'utf-8') as fp:
            json.dump([book.__dict__ for book in self.books], fp,ensure_ascii=False,indent=2)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            books_data = json.load(f)
            self.books = [Book(**data) for data in books_data]

    def search(self, query):
        return [book for book in self.books if query.lower() in book.title.lower()]


library = Library()


book1 = EntityFactory.create_book("Преступление и наказание", "Достоевский Ф.М.")
book2 = EntityFactory.create_book("Generation <<П>>", "Пелевин В.О.")
library.add_book(book1)
library.add_book(book2)

library.save_to_file('library.json')
library.load_from_file('library.json')

found_books = library.search("Преступление и наказание")
for book in found_books:
    print(f'Found book: {book.title} by {book.author}')