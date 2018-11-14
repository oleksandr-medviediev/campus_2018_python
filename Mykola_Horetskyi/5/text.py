load_or_new_game_prompt = """Enter 'load' to load last save or just anything else to start new one."""

start = """While your country goes through economic recession, you're fired from your job.
Entangled in debt, with no money to pay for food or rent, it seems that you have only two choices:either to sell your kidney or to find tresure.
Luckily there are quite a few dungeons near your town."""

go_to_dungeon = ["""After a two-hour ride from the town and three hours of wandering around the forest you finally find what you're looking for under the big old oak.""",
                        """You reckon that the basement in building you live in is rather old.
 Who knows, maybe there are some treasures too, in any case you won't have to spent a lot of time to check.
 You go down into the basement""",
                        """After some googling you find dungeon that you're looking for.
 You take an uber to your destination and finally arrive one hour later."""
                        """Thinking about treasures and careferee life that would follow afterwards you fall asleep.
But the place you wake up in is certainly not your appartment.""",
                        "You go to the place you choose.",
                        "You pack up and set off to the dungeon. Days passed and finally you have arrived."]

enter_dungeon = ["""You see a stone door before you with something written on it in unknown to you language.
After many unsuccessful attempts to open it you give up and decide to watch some movies on your smartphone.
Surprisingly, when protagonists in movie manage to open the door by incidentally saying the password, your door opens too. Why would that happen?""",
                        """There is a dark eerie entrance before you, leading into the unknown.
 The unknown that probably filled with treasures. You master your resolve and step in.""",
                        """Before you is a regular door. Seems too dull for the dungeon.
 Whatever. You enter.""",
                        """There is a big metal door before you with no obvious way to open it exept by using an enormous amount of explosives.
You spend quite a bit of time before discovering some kind of control panel. After pushing a few random buttons the door opens with raspy screech and you enter.""",
                        """There is a gleaming portal before you. Hoping that you'll be able to get back through it, you relucantly step into the light."""]

entrance = "entrance"

enter_room = "You enter the room from the {}."

tell_position = "It's coordinates are {},{}."

no_encounter = ["Room is empty exept for some broken pieces of furniture and you."]

trap_encounter = ["""Suddenly a bunch of goblins rush at you from the shadows.
You try resist but quickly overwhelmed. It's to late to wish for armor and shortsword.""",
                  "You fall into bottomless pit",
                  "You hear a grinding sound below you and realize that you've stepped on a trap.",
                  "A landmine explodes as you step on it.",
                  "You certainly didn't expect the Spanish Inquisition.",
                  "A raspy blade comes swinging from the gap in the wall",
                  """You are very surprised to see the ogre.
Ogre is very surprised to see you. And also very hungry""",
                  """There is a crap in the room. Rather big one.
But still, what can it do to you, pinch your toe?""",
                  """You find a skeleton. Spooky.
Even more spookier when it starts to move a picks up the sword"""]


treasure_encounter = ["You find treasure. You are rich!",
                      "You find a chest filled with gold",
                      """You find a skeleton. Spooky.
But there is expencive looking ring on one of it's fingers. You take it."""]

adjacent_trap = ["You fell danger lurking nearby.",
                 "The passages leading from this room have an eerie feel about them."]

adjacent_treasure = ["You have a feeling in your gut that treasure is nearb.y",
                     "Something tells you that the treasure is near."]

also = ["But that's not all.", "But there's also something else."]

legend_prompt = "Enter l to view legend"

legend = "\n".join(["p - player",
                   "? - unknown tiles",
                   "0 - tiles not bordering any trap or treasure",
                   "1 - tiles bordering treasure",
                   "2 - tiles bordering trap",
                   "3 - tiles bordering both trap and treasure"])

action_prompt = "You decide to "

action_wrong = "\n".join(["You can't do that. You can hovewer:",
                              " w.'go north'",
                              " d. 'go east'",
                              " s. 'go south'",
                              " a. 'go west'",
                              " m. 'view map'",
                              "sv. 'save'",
                              "ld. 'load;"
                         "Just type appropriate action or corresponding letter(s)"])

won = ["""You can hardly can belive it, but it seems you've found all
 treasure in this dungeon. The task of taking it back somehow doesn't seem hard at all."""]

lost = ["YOU DIED"]

no_passage = ["You can't go there.",
              "You carefully check the wall but there doesn't seem to be any passage.",
              "There is just a wall in that direcion."]

game_statistics = "You have found {} treasure out of {}"

end_map_description = """Here is the map of the dungeon.
p - starting position of the player
0 - empty room
t - treasure
# - trap"""


play_again_prompt = "Would you like to play again?"

play_again_hint = " ".join(["Incorrect input. Enter 'y' or 'yes' to play again.",
                           "Enter 'n' or 'no' on first try or any input other",
                           "than 'y' or 'yes' on second (now) to stop playing"])

dungeon_size_promt = "How big would you like the dungeon to be:"

dungeon_size_hint = "Incorrect input. Please enter number between 5 and 50:"

fall_asleep_1= ["You decide to take a break and fall asleep.",
                "Feeling a little tired you fall asleep.",
                "You take a nap."]

fall_asleep_2 =["Id doesn't last long and you wake up feeling uneasy.",
                "Nothing disturbs as you dream of treasures and happy life.",
                "You dream of something scary and wake up in cold sweat"]

load_game_ingame = ["""Suddenly you wake up, realizing that that all that happened before was just a dream.""",
                    """You wake in a wagon, realising your hands are tied up. It's snowing and rather cold for your current attire.
A bearded man sitting near you says, noticing that you woke up:
 - Hey you, you’re finally awake. You were trying to cross the border right?
Walked right into that Imperial ambush same as us and that thief over there..
Realizing this is just another dream, you wake up for real."""]

load_game_start = ["You wake up, remembering that you've beeen exploring dungeon.",
                   "You wake up after well deserved rest. Adventure awaits!"]

enter_room_wake_up = ["the small alcove you set your makeshift bed in.",
                      "adjacent room you've barricaded yourself in before going to sleep."]

no_save_file_ingame = ["You come to realization that this is only reality that exists for you.",
                       "No matter how you wish you were in other place right now, you have to face harsh reality."]
