from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.testingHero = Hero("Super Women", 100, 100.0, 20.0)

    def test_Hero_initialization(self):
        self.assertEqual("Super Women", self.testingHero.username)
        self.assertEqual(100, self.testingHero.level)
        self.assertEqual(100.0, self.testingHero.health)
        self.assertEqual(20.0, self.testingHero.damage)

    def test_hero_description(self):
        expected = f"Hero Super Women: 100 lvl\nHealth: 100.0\nDamage: 20.0\n"
        self.assertEqual(expected, str(self.testingHero))

    def test_hero_fighting_raise_mistakes_fight_with_yourself(self):
        enemy_character = Hero("Super Women", 200, 100.0, 20.0)

        self.assertEqual("Super Women", self.testingHero.username)
        with self.assertRaises(Exception) as context:
            self.testingHero.battle(enemy_character)
        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_hero_fighting_raise_negative_or_zero_health(self):
        enemy_character = Hero("Enemy", 200, 100.0, 20.0)

        self.testingHero.health = 0
        self.assertEqual(0, self.testingHero.health)
        with self.assertRaises(Exception) as context:
            self.testingHero.battle(enemy_character)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))
        self.assertEqual(0, self.testingHero.health)

        self.testingHero.health = -10
        self.assertEqual(-10, self.testingHero.health)
        with self.assertRaises(Exception) as context:
            self.testingHero.battle(enemy_character)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))
        self.assertEqual(-10, self.testingHero.health)

    def test_enemy_fighting_raise_negative_or_zero_health(self):
        enemy_character = Hero("Enemy", 200, -100.0, 20.0)

        self.assertEqual(100, self.testingHero.health)
        self.assertEqual(-100, enemy_character.health)

        with self.assertRaises(Exception) as context:
            self.testingHero.battle(enemy_character)

        self.assertEqual(f"You cannot fight Enemy. He needs to rest", str(context.exception))
        self.assertEqual(100, self.testingHero.health)
        self.assertEqual(-100, enemy_character.health)

        enemy_character_2 = Hero("Enemy", 200, 0.0, 20.0)
        self.assertEqual(0, enemy_character_2.health)

        with self.assertRaises(Exception) as context:
            self.testingHero.battle(enemy_character_2)

        self.assertEqual(f"You cannot fight Enemy. He needs to rest", str(context.exception))
        self.assertEqual(100, self.testingHero.health)
        self.assertEqual(0, enemy_character_2.health)

    def test_hero_fighting_and_drawn(self):
        enemy_character = Hero("Enemy", 20, 2000.0, 5.0)
        result = self.testingHero.battle(enemy_character)
        self.assertEqual("Draw", result)
        self.assertEqual(0, self.testingHero.health)
        self.assertEqual(0, enemy_character.health)

    def test_hero_fighting_and_drawn_below_zero(self):
        enemy_character = Hero("Enemy", 100, 100.0, 20.0)
        result = self.testingHero.battle(enemy_character)
        self.assertEqual("Draw", result)
        self.assertEqual(-1900, self.testingHero.health)
        self.assertEqual(-1900, enemy_character.health)


    def test_hero_fighting_and_win(self):
        enemy_character = Hero("Enemy", 20, 1900.0, 1.0)
        result = self.testingHero.battle(enemy_character)
        self.assertEqual("You win", result)
        self.assertEqual(85, self.testingHero.health)
        self.assertEqual(-100, enemy_character.health)
        self.assertEqual(101, self.testingHero.level)
        self.assertEqual(25, self.testingHero.damage)


    def test_hero_fighting_and_lose(self):
        enemy_character = Hero("Enemy", 10, 2100.0, 10.0)
        result = self.testingHero.battle(enemy_character)
        self.assertEqual("You lose", result)
        self.assertEqual(0, self.testingHero.health)
        self.assertEqual(105, enemy_character.health)
        self.assertEqual(11, enemy_character.level)
        self.assertEqual(15, enemy_character.damage)

if __name__ == '__main__':
    main()