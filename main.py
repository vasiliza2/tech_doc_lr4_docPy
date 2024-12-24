from library import Library
from book import Book
from member import Member

def main():
    """Основная функция для запуска программы."""
    library = Library()

    # Добавление книг
    book1 = Book("1984", "George Orwell", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    library.add_book(book1)
    library.add_book(book2)

    # Добавление членов
    member1 = Member("Alice", 1)
    member2 = Member("Bob", 2)
    library.add_member(member1)
    library.add_member(member2)

    # Проверка выдачи книги
    print(library.check_out_book(1, "1234567890"))  # Alice checks out 1984
    print(library.check_out_book(2, "1234567890"))  # Bob tries to check out 1984 again

    # Возврат книги
    print(library.return_book("1234567890"))  # Return 1984
    print(library.check_out_book(2, "1234567890"))  # Bob checks out 1984

if __name__ == "__main__":
    main()