class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills : dict = {}
        self.guild = "Unaffiliated"

    def player_info(self):
        result = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
        for skill_name, skill_mana  in self.skills.items():
            result += f"==={skill_name} - {skill_mana }\n"
        return result

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cost
            return  f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

