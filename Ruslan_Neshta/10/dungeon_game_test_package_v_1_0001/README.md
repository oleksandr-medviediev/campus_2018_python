# Dungeon Game

It's a simple console game.
There is a map x * x squares.
Map contains randomly placed x * x / 10 traps.
Map contains randomly placed x * x / 20 treasures.

Player starts at a random square, that is not a trap or a treasure.
Player can move up, down, left and right (if it's not an edge of the map).
Player is warned if there's a trap within one square from him.
Player i warned if there's a treasure within one square from him.

If a player get trapped - he loses 1 hp (if 0 - he lost),
if a player finds a treasure - he get +1 to his bag (if 3 - he won).
At start player has hp=3 and a bag=0.

### Prerequisites

1. Download python 3.7 from official [website](https://www.python.org/downloads/).
2. Install python. You can follow this [manual](https://realpython.com/installing-python/) if you need some help with installation.
3. Profit. You can play dungeon game now!

## Authors

* **Ruslan Neshta** - *Initial work* - [s1lence](https://github.com/s1lence)

See also the list of [contributors](https://github.com/oleksandr-medviediev/campus_2018_python/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgments

* Thanks to [Oleksandr Medviediev](https://github.com/oleksandr-medviediev) who created the task
