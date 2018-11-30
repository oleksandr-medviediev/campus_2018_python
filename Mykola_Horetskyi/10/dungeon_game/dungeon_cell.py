from decorator import debug_decorator
import text


class DungeonCell:

    @debug_decorator
    def __init__(self, legend, description):
        """
        DungeonCell class constructor
        """
        self.legend = legend
        self.encounter_description = description


unassigned_cell = DungeonCell("-", text.unassigned_cell_description)

entrance_cell = DungeonCell("e", text.entrance_cell_description)

empty_cell = DungeonCell("0", text.empty_cell_description)

treasure_cell = DungeonCell("x", text.treasure_description)
