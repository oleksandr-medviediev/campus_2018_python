from decorator import debug_decorator
from dungeon_cell import DungeonCell
from random import choice
import text


trap_types = ("arcane", "device", "monster", "unusual","ultimate")


class Trap(DungeonCell):

    @debug_decorator
    def __init__(self, trap_type, legend, description,
    fight_description, survive_description, defeat_description):
        """
        Trap class constructor
        """
        super().__init__(legend, description)
        self.enemy_type = trap_type
        self.fight_description = fight_description
        self.survive_description = survive_description
        self.defeat_description = defeat_description


trap_goblins = Trap("monster","g", text.goblins_encounter, text.goblins_fight,\
text.goblins_survival, text.goblins_defeat)

trap_hidden_blade = Trap("device", "b", text.hiden_blade_encounter,\
text.hidden_blade_fight, text.hidden_blade_survival, text.hidden_blade_defeat)

trap_curse = Trap("magic", "c", text.curse_encounter,\
text.curse_fight, text.curse_survival, text.curse_defeat)

trap_gazebo = Trap("unusual", "g", text.gazebo_encounter,\
text.gazebo_fight, text.gazebo_survival, text.gazebo_defeat)

trap_inquisition = Trap("unusual", "i", text.inquisition_encounter,\
text.inquisition_fight, text.inquisition_survival, text.inqusition_defeat)


trap_legends = (trap_goblins.legend, trap_hidden_blade.legend,\
trap_curse.legend, trap_gazebo.legend)


class Trap(DungeonCell):


    @debug_decorator
    def generate_traps(trap_number):
        """
        Generates trap_number random trap legends

        param: trap_number (int) number of traps to be generated

        returns: list of legends of traps
        """
        traps = []

        while trap_number > 0:
            traps.append(choice(trap_legends))
            trap_number -= 1

        return traps
