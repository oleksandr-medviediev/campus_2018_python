# Dungeon Game

Dungeon Game is a project made with educational purposes while learning python 3.x.

## Requirements

Python 3.7, preferably - Windows 10.

## Usage

Console: 
```bash
python -m main
```

Python:
```python
import main

main.main()
```

## Contents of the package

For more descriptive docs about something specific - look in the code(it contains docs).

1) main.py - wrapper to start game.
2) savegame_utility.py - contains save/load functions.
3) game_enemy.py - Enemy class & necessary info for enemy like phrases.
4) game_exceptions.py - all game-defined exceptions.
5) game_map.py - Position class which describes 2D coordinates(basically contains x,y), Map class. 
6) game_world.py - GameWorld class which represents Duncgeon Game state at some point in time.
7) logging_utiliy.py - contains game logger.
8) map_generator.py - batch of generator functions for map.
9) player.py - PLayer class.

## License
[MIT](https://choosealicense.com/licenses/mit/)
