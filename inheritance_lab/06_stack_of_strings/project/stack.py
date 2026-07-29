class Stack:
    def __init__(self) -> None:
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self) -> int | str :
        if self.is_empty():
            return "List is empty"

        element = self.data[-1]
        del self.data[-1]
        return element


    def top(self) -> int | str :
        if self.is_empty():
            return "List is empty"
        else:
            return self.data[-1]



    def is_empty(self) -> bool:
        if len(self.data) == 0 or self.data is None:
            return True
        return False

    def __str__(self) -> str:
        return f"[{', '.join(reversed(self.data))}]"
