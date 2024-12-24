class Book:
    """
    Класс, представляющий книгу в библиотеке.

    Attributes:
        title (str): Название книги.
        author (str): Автор книги.
        isbn (str): ISBN книги.
        is_checked_out (bool): Статус книги (взята/доступна).
    """

    def __init__(self, title, author, isbn):
        """
        Инициализация книги.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            isbn (str): ISBN книги.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def check_out(self):
        """Проверяет книгу на выдачу."""
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        """Возвращает книгу в библиотеку."""
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

    def __str__(self):
        """Возвращает строковое представление книги."""
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"