from dungeon_logging import logger, methods_with_logging


@methods_with_logging
class Player:

    def __init__(self, name):
        self.name = name
        self.position = [0, 0]

        self._hp = 3
        self._bag = 0

    def get_neighbor_within(self, dx, dy):
        return [self.position[0] + dx, self.position[1] + dy]

    def is_standing_at(self, x, y):
        return self.position == [x, y]

    def is_dead(self):
        return self._hp == 0

    def hurt(self, offender):
        if not self.is_dead():
            self._hp -= 1
            logger.warning('You got hurt by {}. You left with {} hp'.format(offender, self._hp))

    def pickup_treasure(self):
        self._bag += 1
        logger.warning('You picked up treasure. You got {} treasures'.format(self._bag))

    def is_rich(self):
        return self._bag >= 3
