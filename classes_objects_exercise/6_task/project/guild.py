from project import Player

class Guild:
    def __init__(self, name: str):
        self.name = name
        self.player : list[Player] = []

    def assign_player(self, player: Player):
        if player in self.player:
            return f"Player {player.name} is already in the guild."


        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."


        self.player.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"


    def kick_player(self,player_name: str):
        current_player = next((pl for pl in self.player if pl.name == player_name), None)
        if current_player:
            self.player.remove(current_player)
            current_player.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."


    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for pl in self.player:
            result += f'{pl.player_info()}'
        return result

