
# Лабораторная работа 4: Pydoc & JavaDoc


## Введение
В данной лабораторной работе изучаются методы генерации документации для программных проектов с использованием Python и JavaDoc. Основное внимание уделяется инструментам Pydoc для Python и стандартным методам документирования в JavaDoc. Цели работы включают изучение процесса написания документации, её генерацию и публикацию на GitHub Pages.

## Ход работы
### 1) Python и Pydoc
1. Проект library_managment, который позволяет функционировать библиотеке. Он содержит в себе различные классы и функции, отвечающие за добавление книг, новых членов библиотеки, проверку выдачи книг, возврат книг.
2. Пример docstring в коде: 
```python
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
```
3. Используем команду для генерации документации: 
   ```bash
   python -m pydoc -w main
   python -m pydoc -w book
   python -m pydoc -w library
   python -m pydoc -w member
   ```
4. Сгенерированные HTML-файлы были сохранены в папке docs, а затем загружены на GitHub.
Документация была опубликована на GitHub Pages через настройки репозитория.
5. Возникшие проблемы и способы их решения: Проблем при генерации документации и её публикации не возникло
### 2) Java и JavaDoc
1. Проект library_managment, который позволяет функционировать библиотеке. Он содержит в себе различные классы и функции, отвечающие за добавление книг, новых членов библиотеки, проверку выдачи книг, возврат книг.
2. Пример документации класса:
```java
/**
 * Класс, представляющий книгу в библиотеке.
 */
public class Book {
    private String title;
    private String author;
    private String isbn;
    private boolean isCheckedOut;

    /**
     * Инициализация книги.
     *
     * @param title Название книги.
     * @param author Автор книги.
     * @param isbn ISBN книги.
     */
    public Book(String title, String author, String isbn) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.isCheckedOut = false;
    }

    /**
     * Получает название книги.
     *
     * @return Название книги.
     */
    public String getTitle() {
        return title;
    }

    /**
     * Получает автора книги.
     *
     * @return Автор книги.
     */
    public String getAuthor() {
        return author;
    }

    /**
     * Получает ISBN книги.
     *
     * @return ISBN книги.
     */
    public String getIsbn() {
        return isbn;
    }

    /**
     * Проверяет книгу на выдачу.
     *
     * @return true, если книга успешно выдана; false, если книга уже выдана.
     */
    public boolean checkOut() {
        if (!isCheckedOut) {
            isCheckedOut = true;
            return true;
        }
        return false;
    }

    /**
     * Возвращает книгу в библиотеку.
     *
     * @return true, если книга успешно возвращена; false, если книга не была выдана.
     */
    public boolean returnBook() {
        if (isCheckedOut) {
            isCheckedOut = false;
            return true;
        }
        return false;
    }

    @Override
    public String toString() {
        return title + " by " + author + " (ISBN: " + isbn + ")";
    }
}
```
   
  

3. Для генерации документации (Метод 1) был использован стандартный инструмент Javadoc. Команда:
  ```bash
  javadoc -d docs -sourcepath . Main.java Rectangle.java Circle.java Shape.java
  ```
4. Для генерации документации (Метод 2) был использован Maven с плагином `maven-javadoc-plugin`. Однако в данном случае генерация была выполнена вручную.
## Выводы
В ходе лабораторной работы были изучены инструменты для генерации документации для проектов на Python и Golang. 

**Сравнение инструментов Pydoc и Javadoc**:
  Pydoc и Javadoc являются мощными инструментами для генерации документации на Python и Java соответственно. Оба инструмента генерируют HTML-файлы, которые можно легко опубликовать. Pydoc проще в использовании, но Javadoc предлагает более мощные возможности по настройке через Maven.
**Анализ и выводы о необходимости документации в разработке**:
  Документация играет ключевую роль в поддержке и использовании кода другими разработчиками. Хорошо написанная документация значительно упрощает понимание проекта, его расширение и поддержку.

**Выводы о балансе между документированием и самодокументирующимся кодом**:
  Хотя самодокументирующийся код важен (то есть код, понятный без дополнительного объяснения), наличие детализированных комментариев и документированных интерфейсов критично для больших проектов. Документация помогает сократить время на изучение чужого кода.

**Возможные улучшения и дальнейшие шаги**:
  - В будущем можно использовать Sphinx для создания более детализированной документации для Python.
  - Автоматизация деплоя документации с помощью GitHub Actions также может повысить эффективность работы.


## Ссылки
1. Python: https://elyakkos.github.io/techdoc-lr4-DocPy/docs/ (cсылка на документацию)
2. Java: https://elyakkos.github.io/techdoc-lr4-javadoc/docs/package-summary.html (ссылка на документацию)
3. Руководство по написанию документации Python: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
4. Официальный гайд от авторов языка о правильном написании комментариев: [Go Comment Guide](https://go.dev/doc/comment).
