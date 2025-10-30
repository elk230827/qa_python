from pytest import Collector
from fixtures import BOOK, GENRE
from main import BooksCollector
import pytest

BOOK = 'Гордость и предубеждение и зомби'
GENRE = 'Фантастика'


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2

    def test_get_book_genre_positive(self):
        collector = BooksCollector()

        collector.add_new_book(BOOK)
        collector.set_book_genre(BOOK, GENRE)

        assert collector.get_book_genre(BOOK) == GENRE  

    def test_set_book_genre_one_genre(self):
        collector = BooksCollector()
        collector.add_new_book(BOOK)
        collector.set_book_genre(BOOK, GENRE)


        assert collector.books_genre[BOOK] == GENRE

    def test_get_books_with_specific_genre_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book(BOOK)
        collector.set_book_genre(BOOK, GENRE)
        
        res = collector.get_books_with_specific_genre(GENRE)

        assert res[0] == BOOK

    def test_get_books_for_children_positive(self):
        collector = BooksCollector()

        books = ['Книга детектив', 'Книга ужасы', 'Книга детская']
        genre = 'Фантастика'
        collector.add_new_book(books[0])
        collector.set_book_genre(books[0], 'Детектив')
        collector.add_new_book(books[1])
        collector.set_book_genre(books[1], 'Ужасы')
        collector.add_new_book(books[2])
        collector.set_book_genre(books[2], 'Фантастика')
        res = collector.get_books_for_children()

        assert res[0] == books[2]

    def test_add_book_in_favorites_positive(self):
        collector = BooksCollector()
        collector.add_new_book(BOOK)
        collector.set_book_genre(BOOK, GENRE)

        collector.add_book_in_favorites(BOOK)
        
        assert collector.favorites[0] == BOOK

    def test_delete_book_from_favorites_positive(self):
        collector = BooksCollector()
        collector.add_new_book(BOOK)
        collector.set_book_genre(BOOK, GENRE)
       
        collector.add_book_in_favorites(BOOK)
        collector.delete_book_from_favorites(BOOK)
        
        assert len(collector.favorites) == 0

    def test_set_book_genre_wrong_genre(self):
        collector = BooksCollector()
        collector.add_new_book(BOOK)
        collector.set_book_genre(BOOK, GENRE)
 
        collector.set_book_genre(BOOK, 'Мелодрама')
        assert collector.books_genre[BOOK] == GENRE

    def test_add_book_in_favorites_wrong_book(self):
        collector = BooksCollector()
        collector.add_new_book(BOOK)
        collector.set_book_genre(BOOK, GENRE)
 
        collector.add_book_in_favorites('Неправильная книга')
        assert len(collector.favorites) == 0

    def test_get_book_genre_wrong_book(self):
        collector = BooksCollector()
        collector.add_new_book(BOOK)
        collector.set_book_genre(BOOK, GENRE)
 
        res = collector.get_book_genre('Неправильная книга') 
        assert res == None     
