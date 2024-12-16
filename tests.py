from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг


    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_with_name_exceeded_maximum_length_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('Энциклопедия знаков, символов, фамилий!))')

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_genre_added(self, collector, add_genre):
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Комедии'


    def test_set_book_invalid_genre_not_added(self, collector):
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Драмы')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''


    def test_get_books_with_specific_genre_one_book_received(self, collector, add_genre):
        assert len(collector.get_books_with_specific_genre('Комедии')) == 1


    def test_get_books_for_children_one_book_received(self, collector, add_genre):
        assert len(collector.get_books_for_children()) == 1

    def test_get_books_for_children_non_children_genre(self, collector):
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert len(collector.get_books_for_children()) == 0

    def test_get_books_for_children_genre_not_list_returns_empty_list(self, collector):
        assert len(collector.get_books_for_children()) == 0


    def test_add_book_in_favorites_add_book_book_added(self, collector, add_genre):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_book_returns_empty_list(self, collector, add_genre):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 0
