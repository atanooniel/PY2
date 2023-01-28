class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        # блок проверок входных данных
        if not isinstance(name, str):
            raise ValueError('Название книги должно быть передано в строковом формате')
        if not isinstance(author, str):
            raise ValueError('Автор должен быть передан в строковом формате')
        self._name = name
        self._author = author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # наследуюем конструктор родительского класса
        self.pages = pages  # дополняем конструктор родительского класса

    def __repr__(self) -> str:  # перегруженный метод для дочернего класса
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages) -> None:
        # блок проверок входных данных
        if not isinstance(pages, int):
            raise ValueError('Страницы должны быть переданы целым числом')
        if not pages > 0:
            raise ValueError('Страницы должны быть положительным числом')
        self._pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # наследуюем конструктор родительского класса
        self.duration = duration  # дополняем конструктор родительского класса

    def __repr__(self) -> str:  # перегруженный метод для дочернего класса
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        # блок проверок входных данных
        if not isinstance(duration, float):
            raise ValueError('Длительность должна быть передана вещественным числом')
        if not duration > 0:
            raise ValueError('Длительность должна быть положительным числом')
        self._duration = duration
