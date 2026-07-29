from project import Album
class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: list[Album] = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."


    def remove_album(self, album_name: str):
        current_album = next(filter(lambda x: x.name == album_name, self.albums), None)
        if current_album:
            if current_album.published:
                return f"Album has been published. It cannot be removed."

            self.albums.remove(current_album)
            return f"Album {current_album.name} has been removed."

        return f"Album {album_name} is not found."


    def details(self):
        result = ""
        for album in self.albums:
            result += album.details() + "\n"

        return f"Band {self.name}\n{result}"


