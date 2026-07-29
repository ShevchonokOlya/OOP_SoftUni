from project import Room


class Hotel:
    def __init__(self, name:str)->None:
        self.name = name
        self.rooms : list[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people:int) -> None:
        for room in self.rooms:
            if room.number == room_number:
                if room.take_room(people) is None:
                    self.guests += people

    def free_room(self, room_number: int) -> None:
        room = next((r for r in self.rooms if room_number == r.number), None)
        if room:
            self.guests -= room.guests
            room.free_room()


    def status(self):
        taken_room = [str(r.number) for r in self.rooms if r.is_taken]
        free_room = [str(r.number) for r in self.rooms if r.is_taken == False]
        result = f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(free_room)}\nTaken rooms: {', '.join(taken_room)}"
        return result
