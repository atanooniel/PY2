BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_  # Идентификатор книги
        self.name = name  # Название книги
        self.pages = pages  # Количество страниц в книге

    def __str__(self):
        """
        :return: Вывод в формате: Книга "название_книги"
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        :return: Вывод в формате: Book(id_=1, name='test_name_1', pages=200)
        """
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books: [Book] = []):
        self.books = books

    def get_next_book_id(self):
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.

        :return:
        Если книг в библиотеке нет, возвращает 1.
        Если книги есть, возвращает идентификатор последней книги увеличенный на 1.
        """
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int):
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.

        :param book_id: идентификатор книги для поиска
        :return:
        Если книга существует, возвращает индекс из списка.
        Если книги нет, вызывает ошибку ValueError с сообщением: "Книги с запрашиваемым id не существует"
        """
        for index, book in enumerate(self.books):
            if book_id == book.id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
