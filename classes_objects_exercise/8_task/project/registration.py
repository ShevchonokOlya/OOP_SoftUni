from project import Library
from project import User


class Registration:
    def __init__(self):
        pass

    @staticmethod
    def add_user(user: User, library: Library) -> None | str:

        for current_user in library.user_records:
            if current_user.user_id == user.user_id:
                return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)
        return None

    @staticmethod
    def remove_user(user: User, library: Library) -> None | str:
        if user in library.user_records:
            library.user_records.remove(user)
            return None
        return "We could not find such user to remove!"

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library):
        target_user = next((current_user for current_user in library.user_records if current_user.user_id == user_id), None)
        if target_user:
            if target_user.username != new_username:
                old_username = target_user.username
                target_user.username = new_username

                if old_username in library.rented_books:
                    library.rented_books[new_username] = library.rented_books.pop(old_username)
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
            else:
                return "Please check again the provided username - it should be different than the username used so far!"

        return f"There is no user with id = {user_id}!"


