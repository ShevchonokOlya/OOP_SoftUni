
from project import User

class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict[str, list[str]] = {}
        self.rented_books: dict[str, dict[str, int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str | None:
        if author in self.books_available.keys() and book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username not in self.rented_books.keys():
                self.rented_books[user.username] = {}

            self.rented_books[user.username][book_name] = days_to_return

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for rented_user, books_data in self.rented_books.items():
            if book_name in books_data:
                return f'The book "{book_name}" is already rented and will be available in {books_data[book_name]} days!'
        return None

    def return_book(self, author: str, book_name: str, user: User) -> str | None:
        if book_name in user.books:
            user.books.remove(book_name)

            if author not in self.books_available:
                self.books_available[author] = []

            self.books_available[author].append(book_name)
            self.rented_books[user.username].pop(book_name)
            return None

        return f"{user.username} doesn't have this book in his/her records!"



