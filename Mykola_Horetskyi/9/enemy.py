from decorator import debug_decorator
from character import Character
import text

enemy_types = ("arcane", "device", "monster", "unusual", "ultimate")


class Enemy:

    @debug_decorator
    def __init__(self, name, enemy_type, legend, encounter_description,
    fight_description, survive_description, defeat_description):
        """
        Enemy class constructor.
        """
        super().__init__()
        self.name = name
        self.enemy_type = enemy_type
        self.legend = legend
        self.encounter_description = encounter_description
        self.fight_description = fight_description
        self.survive_description = survive_description
        self.defeat_description = defeat_description


enemy_inquisition = Enemy("Spanish Inquisition","ultimate", "I",\
text.inquisition_encounter,text.inquisition_fight,\
 text.inquisition_survival, text.inqusition_defeat)

enemies_list = [enemy_inquisition]
