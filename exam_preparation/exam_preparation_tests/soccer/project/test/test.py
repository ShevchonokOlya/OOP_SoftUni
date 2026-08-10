from project.soccer_player import SoccerPlayer
from unittest import TestCase, main


class TestSoccerPlayer(TestCase):
    def setUp(self):
        self.player = SoccerPlayer("Joseph", 20, 50, "Juventus")

    def test_init(self):
        self.assertIsInstance(self.player, SoccerPlayer)
        self.assertEqual("Joseph", self.player.name)
        self.assertEqual(20, self.player.age)
        self.assertEqual(50, self.player.goals)
        self.assertEqual("Juventus", self.player.team)

        self.assertTrue(isinstance(self.player.achievements, dict))
        self.assertEqual(0, len(self.player.achievements))

    def test_name_setter_valid_value(self):
        self.player.name = "Joseph"
        self.assertEqual("Joseph", self.player.name)
        self.player.name = "Juventus"
        self.assertEqual("Juventus", self.player.name)
        self.player.name = "  Juv "
        self.assertEqual("  Juv ", self.player.name)

        self.player.name = "      "
        self.assertEqual("      ", self.player.name)

    def test_name_setter_invalid_value(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = "Juv"
        self.assertEqual("Name should be more than 5 symbols!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.player.name = "12345"
        self.assertEqual("Name should be more than 5 symbols!", str(ex.exception))

    def test_age_setter_valid_value(self):
        self.player.age = 16
        self.assertEqual(16, self.player.age)

        self.player.age = 100
        self.assertEqual(100, self.player.age)


    def test_age_setter_invalid_value(self):
        with self.assertRaises(ValueError) as ex:
            self.player.age = 15
        self.assertEqual("Players must be at least 16 years of age!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.player.age = -100
        self.assertEqual("Players must be at least 16 years of age!", str(ex.exception))

    def test_goals_setter_valid_value(self):
        self.player.goals = -1
        self.assertEqual(0, self.player.goals)

        self.player.goals = 100
        self.assertEqual(100, self.player.goals)


    # def test_goals_setter_invalid_value(self):
    #     self.player.goals = False
    #     self.assertEqual(0, self.player.goals)

    def test_team_setter_valid_value(self):
        self.player.team = "Barcelona"
        self.assertEqual("Barcelona", self.player.team)

        self.player.team = "Manchester United"
        self.assertEqual("Manchester United", self.player.team)


    def test_team_setter_invalid_value(self):

        with self.assertRaises(ValueError) as ex:
            self.player.team =  None
        self.assertEqual(f"Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.player.team =  "None"
        self.assertEqual(f"Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.player.team =  ""
        self.assertEqual(f"Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.player.team =  'Juventus '
        self.assertEqual(f"Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!", str(ex.exception))


    def test_Change_team_valid_value(self):
        self.assertEqual("Juventus", self.player.team)
        newTeam = "Manchester United"
        result = self.player.change_team(newTeam)
        self.assertEqual("Manchester United", self.player.team)
        self.assertEqual("Team successfully changed!", result)

    def test_Change_team_invalid_value(self):
        self.assertEqual("Juventus", self.player.team)
        result = self.player.change_team(None)
        self.assertEqual("Invalid team name!", result)
        self.assertEqual("Juventus", self.player.team)

        result2 = self.player.change_team("None")
        self.assertEqual("Invalid team name!", result2)
        self.assertEqual("Juventus", self.player.team)


        result3 = self.player.change_team("Juventus ")
        self.assertEqual("Invalid team name!", result3)
        self.assertEqual("Juventus", self.player.team)

    def test_adding_new_achievement_valid_value(self):

        self.assertEqual(0, len(self.player.achievements))
        ret = self.player.add_new_achievement("Award")
        self.assertEqual("Award has been successfully added to the achievements collection!",  ret )

        self.assertEqual(1, len(self.player.achievements))
        self.assertEqual(1, self.player.achievements["Award"])
        ret2 =self.player.add_new_achievement("Award")
        self.assertEqual("Award has been successfully added to the achievements collection!", ret2)

        self.assertEqual(1, len(self.player.achievements))
        self.assertEqual(2, self.player.achievements["Award"])

        ret3 = self.player.add_new_achievement("Statistical milestones")
        self.assertEqual("Statistical milestones has been successfully added to the achievements collection!", ret3)

        self.assertEqual(2, len(self.player.achievements))
        self.assertEqual(1, self.player.achievements["Statistical milestones"])
    
    def test_comparison_less_than_another(self):
        p1 = SoccerPlayer("Goal50_1", 20, 50, "Juventus")
        p2 = SoccerPlayer("Goal50_2", 20, 50, "Juventus")
        result = p1 < p2
        self.assertEqual(f"Goal50_1 is a better goal scorer than Goal50_2.", result)
        result2 = p1 > p2
        self.assertEqual(f"Goal50_2 is a better goal scorer than Goal50_1.", result2)

        p3 = SoccerPlayer("Goal20", 20, 20, "Juventus")
        p4 = SoccerPlayer("Goal50", 20, 50, "Juventus")

        result3 = p3 < p4
        self.assertEqual("Goal50 is a top goal scorer! S/he scored more than Goal20.", result3)
        result4 = p3 > p4
        self.assertEqual("Goal50 is a better goal scorer than Goal20.", result4)

        p5 = SoccerPlayer("Goal_120", 20, 120, "Juventus")
        p6 = SoccerPlayer("Goal_50", 20, 50, "Juventus")

        result5 = p5 < p6
        self.assertEqual("Goal_120 is a better goal scorer than Goal_50.", result5)
        result6 = p5 > p6
        self.assertEqual("Goal_120 is a top goal scorer! S/he scored more than Goal_50." , result6)


if __name__ == "__main__":
    main()
