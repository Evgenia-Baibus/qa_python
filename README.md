# qa_python

Реализован следующие набор тестов для [BooksCollector](main.py), которые проверяют:
* `test_add_new_book_add_two_books` - проверяет, что при добавлении двух книг в словарь `books_rating` добавляются именно 
две книги 
* `test_add_new_book_with_name_exceeded_maximum_length_not_added` - проверяет, что книга с именем, превышающим максимальную 
допустимую длину, не добавляется в `books_genre` 
* `test_set_book_genre_genre_added` - проверяет, что книге, которая есть в словаре `books_genre` устнавливается жанр из 
списка `genre`  
* `test_set_book_invalid_genre_not_added` - проверяет, что жанр, которого нет в списке `genre`, не устанавливается
* `test_get_books_with_specific_genre_one_book_received` - проверяет, что выводится книга с определенным жанром 
* `test_get_books_for_children_one_book_received` - проверяет, что выводится книга, которая подходит детям
* `test_get_books_for_children_non_children_genre` - проверяет, что книга с возрастным рейтингом отсутствует в списке 
книг для детей
* `test_get_books_for_children_genre_not_list_returns_empty_list` - проверяет, что книга с жанром, которого нет в списке 
`genre` отсутствует в списке книг для детей
* `test_add_book_in_favorites_add_book_book_added` - проверяет, что книга, которая находится в словаре `books_genre`, добавляется в избранное
* `test_delete_book_from_favorites_delete_book_returns_empty_list` - проверяет, что книга, которая есть в избранном удаляется оттуда

P.S.
Методы `get_book_genre` и `get_books_genre` проверены в рамках тестов `test_add_new_book_add_two_books` и `test_set_book_genre_genre_added`


