class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comment: list = []
        self.completed: bool = False

    def change_name(self , new_name: str) -> None | str:
        if new_name != self.name:
            self.name = new_name
            return new_name
        return 'Name cannot be the same.'

    def change_due_date(self, new_date: str) -> None | str:
        if new_date != self.due_date:
            self.due_date = new_date
            return new_date
        return 'Date cannot be the same.'

    def add_comment(self, comment: str) -> None | str:
        self.comment.append(comment)

    def edit_comment(self, comment_number: int,  new_comment: str) -> None | str:
        if 0 <= comment_number < len(self.comment):
            self.comment[comment_number] = new_comment
            return ', '.join(self.comment)

        return "Cannot find comment."

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"


