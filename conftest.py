import pytest

from main import BooksCollector

@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()

    collector.add_new_book('Гордость и предубеждение и зомби')

    return collector

@pytest.fixture(scope='function')
def add_genre(collector):
     collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
     return collector