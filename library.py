from book import Book
from member import Member

class Library:
    """
    Класс, представляющий библиотеку.

    Attributes:
        books (list): Список книг в библиотеке.
        members (list): Список членов библиотеки.
    """

    def __init__(self):
        """Инициализация библиотеки с пустыми списками книг и членов."""
        self.books = []
        self.members = []

    def add_book(self, book):
        """Добавляет книгу в библиотеку.

        Args:
            book (Book): Книга для добавления.
        """
        self.books.append(book)

    def add_member(self, member):
        """Добавляет члена в библиотеку.

        Args:
            member (Member): Член для добавления.
        """
        self.members.append(member)

    def check_out_book(self, member_id, isbn):
        """Выдает книгу члену библиотеки.

        Args:
            member_id (int): Уникальный идентификатор члена.
            isbn (str): ISBN книги.

        Returns:
            str: Сообщение о результате операции.
        """
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if member is None:
            return "Член с таким ID не найден."
        if book is None:
            return "Книга с таким ISBN не найдена."
        if book.check_out():
            return f"Книга '{book.title}' выдана члену '{member.name}'."
        return "Книга уже выдана."

    def return_book(self, isbn):
        """Возвращает книгу в библиотеку.

        Args:
            isbn (str): ISBN книги.

        Returns:
            str: Сообщение о результате операции.
        """
        book = next((b for b in self.books if b.isbn == isbn), None)
        if book is None:
            return "Книга с таким ISBN не найдена."
        if book.return_book():
            return f"Книга '{book.title}' возвращена в библиотеку."
        return "Книга не была выдана."