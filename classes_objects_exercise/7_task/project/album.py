from project import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.songs: list[Song] = list(songs)

    def add_song(self, song: Song):
        if song not in self.songs:
            if self.published:
                return f"Cannot add songs. Album is published."

            if song.single:
                return f"Cannot add {song.name}. It's a single"

            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        else:
            return "Song is already in the album."

    def remove_song(self, song_name: str):
        current_song = next(filter(lambda song: song.name == song_name, self.songs), None)
        if current_song:
            if self.published:
                return f"Cannot remove songs. Album is published."

            self.songs.remove(current_song)
            return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.get_info()}\n"

        return result.strip()
