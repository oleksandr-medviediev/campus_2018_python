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

        load_file = open("file.txt", "r")
        game_matrix = []
    
        data = load_file.readlines()
        load_file.close()

        player_position = []

        for i in range(len(data)):
            line = data[i].split(' ')
            line.pop()

            game_matrix.append(line)

        return game_matrix
