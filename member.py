class Member:
    """
    Класс, представляющий члена библиотеки.

    Attributes:
        name (str): Имя члена.
        member_id (int): Уникальный идентификатор члена.
    """

    def __init__(self, name, member_id):
        """
        Инициализация члена библиотеки.

        Args:
            name (str): Имя члена.
            member_id (int): Уникальный идентификатор члена.
        """
        self.name = name
        self.member_id = member_id

    def __str__(self):
        """Возвращает строковое представление члена библиотеки."""
        return f"{self.name} (ID: {self.member_id})"