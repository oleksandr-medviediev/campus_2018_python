from decorator import debug_decorator
from character import Character
from dungeon_map import DungeonMap

class Player:

    proficiencies = {"melee", "magic", "guile", "none"}

    proficiency_immunity = {
    "melee":"monster",
    "magic":"arcane",
    "guile":"device",
    "none":"unusual"
    }


    def __init__(self):
        """
        Constructor of Player class
        """
        super().__init__()
        self.bag = 0
        self.health = 0
        self.proficiency = ""
        self.discovered_map = DungeonMap()


    @debug_decorator
    def initialize(self, health, position, bag, name, proficiency, discovered_map):
        """
        Initializes Player class
        """
        super().initialize(name, position)
        self.health = health
        self.bag = bag
        self.proficiency = proficiency
        self.discovered_map = discovered_map

    @debug_decorator
    def take_damage(self):
        """
        Reduces health by 1
        """
        self.health -= 1


    @debug_decorator
    def is_alive(self):
        """
        Checks whether Character is is_alive

        returns: bool
        """

        return self.health > 0
