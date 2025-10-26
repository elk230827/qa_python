from pytest import Collector
from main import BooksCollector
import pytest
BOOK = 'Гордость и предубеждение и зомби'
GENRE = 'Фантастика'

@pytest.fixture
def collector_one_book():
    collector = BooksCollector()

    
    collector.add_new_book(BOOK)
    collector.set_book_genre(BOOK, GENRE)
    return collector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_set_one_genre(self, collector_one_book):


        assert collector_one_book.get_book_genre(BOOK) == GENRE

    def test_get_books_with_specific_genre_correct_genre(self,collector_one_book):
        
        
        res = collector_one_book.get_books_with_specific_genre(GENRE)

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

    def test_add_book_in_favorites_positive(self, collector_one_book):
 
        res = collector_one_book.add_book_in_favorites(BOOK)
        res = collector_one_book.get_list_of_favorites_books()
        assert res[0] == BOOK

    def test_get_list_of_favorites_books_positive(self, collector_one_book):
 
        collector_one_book.add_book_in_favorites(BOOK)
        collector_one_book.delete_book_from_favorites(BOOK)
        res = collector_one_book.get_list_of_favorites_books()
        assert len(res) == 0

    def test_set_book_genre_wrong_genre(self, collector_one_book):
 
        collector_one_book.set_book_genre(BOOK, 'Мелодрама')
        assert collector_one_book.get_book_genre(BOOK) == GENRE

    def test_add_book_in_favorites_wrong_book(self, collector_one_book):
 
        res = collector_one_book.add_book_in_favorites('Неправильная книга')
        res = collector_one_book.get_list_of_favorites_books() 
        assert len(res) == 0  

    def test_get_book_genre_wrong_book(self, collector_one_book):
 
        res = collector_one_book.get_book_genre('Неправильная книга') 
        assert res == None     
