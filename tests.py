from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

#тест 1 - устанавливаем рейтинг книге (от 1 до 10)
    def test_set_book_rating_book_rating_2(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # устанавливаем рейтинг книги 'Гордость и предубеждение и зомби' 2
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 2)

        # проверяем, что у книги 'Гордость и предубеждение и зомби' рейтинг равен 2
        assert collector.books_rating.get('Гордость и предубеждение и зомби') == 2

#тест 2 - получаем рейтинг книги по ее имени
    def test_get_book_rating_book_name_rating(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        #задаем рейтинг книги 'Гордость и предубеждение и зомби' 7
        collector.books_rating['Гордость и предубеждение и зомби'] = 7

        # запрашиваем рейтинг книги 'Гордость и предубеждение и зомби'
        collector.get_book_rating('Гордость и предубеждение и зомби')

        # проверяем, что у книги 'Гордость и предубеждение и зомби' рейтинг равен 7
        assert collector.books_rating.get('Гордость и предубеждение и зомби') == 7

#тест 3 - выводим список книг с определенным рейтингом
    def test_get_books_with_specific_rating(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # задаем рейтинг книг
        collector.books_with_specific_rating = []
        collector.books_rating['Гордость и предубеждение и зомби'] = 2
        collector.books_rating['Что делать, если ваш кот хочет вас убить'] = 3
        collector.books_rating['Пролетая над гнездом кукушки'] = 3

        # запрашиваем список книг с рейтингом 3
        collector.get_books_with_specific_rating(3)

        # проверяем список книг с рейтингом 3
        assert collector.get_books_with_specific_rating(3) == ['Что делать, если ваш кот хочет вас убить', 'Пролетая над гнездом кукушки']

#тест 4 - получаем словарь books_rating
    def test_get_books_rating_dict_books_rating(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # задаем рейтинг книг в словаре books_rating
        collector.books_rating['Гордость и предубеждение и зомби'] = 2
        collector.books_rating['Что делать, если ваш кот хочет вас убить'] = 3

        #запрашиваем словарь books_rating
        collector.get_books_rating()

        #проверяем получение словаря books_rating
        assert collector.get_books_rating() == {'Гордость и предубеждение и зомби': 2, 'Что делать, если ваш кот хочет вас убить': 3}

#тест 5 - добавляем книгу в Избранное
    def test_add_book_in_favorites_book_added_in_favorites(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        #добавляем книгу в books_rating
        collector.add_new_book('Пролетая над гнездом кукушки')
        #добавляем книгу в Избранные
        collector.add_book_in_favorites('Пролетая над гнездом кукушки')

        #проверяем, что книга 'Пролетая над гнездом кукушки' в Избранном
        assert 'Пролетая над гнездом кукушки' in collector.favorites

#тест 6 - удаляем книгу из Избранного
    def test_delete_book_from_favorites_book_not_in_favorites(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу в books_rating
        collector.add_new_book('Пролетая над гнездом кукушки')
        # добавляем книгу в Избранные
        collector.add_book_in_favorites('Пролетая над гнездом кукушки')

        #удаляем книгу из Избранного
        collector.delete_book_from_favorites('Пролетая над гнездом кукушки')

        #проверяем, что книга 'Пролетая над гнездом кукушки' удалена из Избранного
        assert 'Пролетая над гнездом кукушки' not in collector.favorites

#тест 7 - получаем список Избранных книг
    def test_get_list_of_favorites_books_get_list_of_favorites_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        #задаем список Избранных книг
        collector.favorites = ['Пролетая над гнездом кукушки','Гордость и предубеждение и зомби']

        #получаем список Избранных книг
        collector.get_list_of_favorites_books()

        #проверяем получение списка Избранных книг
        assert collector.get_list_of_favorites_books() == ['Пролетая над гнездом кукушки','Гордость и предубеждение и зомби']

#тест 8 - проверяем, что книга не добавляется дважды в Избранное
    def test_add_twice_book_in_favorites_book_not_added_twice_in_favorites(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # задачем список Избранных книг
        collector.favorites = ['Пролетая над гнездом кукушки', 'Гордость и предубеждение и зомби']

        #добавляет книгу 'Пролетая над гнездом кукушки' еще раз в Изюранное
        collector.add_book_in_favorites('Пролетая над гнездом кукушки')

        # проверяем, что книга 'Пролетая над гнездом кукушки' в Избранном в 1 количестве
        assert collector.favorites.count('Пролетая над гнездом кукушки') == 1

#тест 9 - проверяем, что рейтинг книгb по умолчанию 1
    def test_get_book_rating_book_rating_1(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу в books_rating
        collector.add_new_book('Гордость и предубеждение и зомби')

        # запрашиваем рейтинг книги 'Гордость и предубеждение и зомби'
        collector.get_book_rating('Гордость и предубеждение и зомби')

        # проверяем, что у книги 'Гордость и предубеждение и зомби' рейтинг равен 1
        assert collector.books_rating.get('Гордость и предубеждение и зомби') == 1

