class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError('Имя книги должно быть строкой')

        if not isinstance(author, str):
            raise TypeError('Автор книги должен быть строкой')

        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга '{self.name}'. Автор {self.author}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

class PaperBook(Book):
    """ Дочерний класс. Бумажная книга """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()} Количество страниц {self.pages}"

    def __repr__(self):
        return f"{super().__repr__()} (pages={self.pages!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook(Book):
    """ Дочерний класс. Аудио книга """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"{super().__str__()} Продолжительность книги {self.duration}"

    def __repr__(self):
        return f"{super().__repr__()} (pages={self.duration!r})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность книги типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность книги не может быть отрицательной")
        self._duration = new_duration

