import unittest
from player import Player

   
class PlayerTest(unittest.TestCase):

    player = Player()

    def setUp(self):
        self.player.hp = 3
        self.player.bag = 0
        print("created test player")

    def tearDown(self):
        print("deleted test player")
    
    def test_pick_treasure(self):
        
        bag = self.player.bag
        self.player.pick_treasure()
        self.assertEqual (bag + 1, self.player.bag)
        
        
    def test_lose_hp(self):
        
        hp = self.player.hp
        self.player.lose_hp()
        self.assertEqual (hp - 1, self.player.hp) 

if __name__ == '__main__':
    unittest.main()        
        