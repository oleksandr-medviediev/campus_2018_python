import dungeon_game_logger as log


class GameIO:
    def save_game(self, game_matrix):
        """
        Save game map in file.

        :param my_map: game area.
        :type my_map: list.

        :return: None.

        """
        save_file = open("file.txt", "w")

        for i in game_matrix:
            string = ' '.join(i) + " \n"
            save_file.write(string)

        save_file.close()


    def load_game(self):
        """
        Load game map from file.

        :return: game map.
        :rtype: list.

        """
        game_matrix = []

        try:
            load_file = open("file.txt", "r")
            
            data = load_file.readlines()
            load_file.close()

            for i in range(len(data)):
                line = data[i].split(' ')
                line.pop()

                game_matrix.append(line)
        except IOError:
            log.logger.error("IOError exception. Could not open file to read data.")

        return game_matrix
