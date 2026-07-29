from project import Player


class Team:
    def __init__(self, name: str, rating: int) -> None:
        self.__name = name
        self.__rating = rating
        self.__players: list[Player] = []

    def add_player(self, player: Player) -> None | str:
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"


    def remove_player(self, player_name: str) -> Player | str:
        target = next((pl for pl in self.__players if pl.name == player_name), None)
        if target:
            self.__players.remove(target)
            return target
        return f"Player {player_name} not found"