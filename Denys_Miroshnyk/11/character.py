
class Character:
    def __init__(self, name):
        self.MAX_HP = 3
        self.current_hp = self.MAX_HP
        self.BACKPACK_MAX = 3
        self.current_backpack = 0
        self.position = [-1, -1]
        self.name = name
    

character = Character("Denys")
