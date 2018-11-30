import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from utils import Position
from game import DungeonGame
from player import Player
from enemy import enemies_list
from trap import traps_list

class HostileEncounterTest(unittest.TestCase):


    def setUp(self):

        self.dungeonGame = DungeonGame()

        DungeonGame.player.health = len(Player.proficiencies)\
                                   * (len(enemies_list) + len(traps_list))


    def testEnemyEncounter(self):

        for proficiency in Player.proficiencies:
            DungeonGame.player.proficiency = proficiency
            player_immunity = Player.proficiency_immunity[proficiency]

            for enemy_character in enemies_list:

                player_health_before = DungeonGame.player.health
                self.dungeonGame.process_hostile_encounter(enemy_character)

                #check that health points decrreased by one if player not immune to enemy
                if (player_immunity != enemy_character.enemy_type):
                    self.assertEqual(player_health_before- 1,\
                     DungeonGame.player.health)

                #otherwise check that health remained the same
                else:
                    self.assertEqual(player_health_before,\
                     DungeonGame.player.health)


    def testTrapEncounter(self):

        for proficiency in Player.proficiencies:
            DungeonGame.player.proficiency = proficiency
            player_immunity = Player.proficiency_immunity[proficiency]

            for trap in traps_list:

                player_health_before = DungeonGame.player.health
                self.dungeonGame.process_hostile_encounter(trap)

                #check that health points decrreased by one if player not immune to trap
                if (player_immunity != trap.enemy_type):
                    self.assertEqual(player_health_before- 1,\
                     DungeonGame.player.health)

                #otherwise check that health remained the same
                else:
                    self.assertEqual(player_health_before,\
                     DungeonGame.player.health)

    def tearDown(self):

        print('Hostile encounter test ended.')


if __name__ == '__main__':
    unittest.main()
