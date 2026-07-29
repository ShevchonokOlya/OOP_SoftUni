from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    VALID_TEAM_NAMES = {"Red Bull" : RedBullTeam , "Mercedes": MercedesTeam}

    def __init__(self):
        self.red_bull_team: RedBullTeam | None = None
        self.mercedes_team: MercedesTeam | None  = None


    def is_valid_team_name(self, team_name: str):
        if team_name in self.VALID_TEAM_NAMES.keys():
            return self.VALID_TEAM_NAMES[team_name]
        return None

    def register_team_for_season(self, team_name: str, budget: int):
        team = self.is_valid_team_name(team_name)
        if team:
            if team.__name__ == "MercedesTeam":
                self.mercedes_team = team(budget)
            elif team.__name__ == "RedBullTeam":
                self.red_bull_team = team(budget)
        else:
            raise ValueError("Invalid team name!")
        return f"{team_name} has joined the new F1 season."


    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if (self.red_bull_team is None) or (self.mercedes_team is None):
            raise Exception("Not all teams have registered for the season.")

        better_team  = "Red Bull" if  red_bull_pos < mercedes_pos else "Mercedes"
        rb_rev = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        merc_rev = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        return f"Red Bull: {rb_rev}. Mercedes: {merc_rev}. {better_team} is ahead at the {race_name} race."