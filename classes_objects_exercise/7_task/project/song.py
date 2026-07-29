class Song:
    def __init__(self, title: str, length: float, single: bool):
        self.name = title
        self.length = length
        self.single = single

    def get_info(self):
        return f"{self.name} - {self.length}"
