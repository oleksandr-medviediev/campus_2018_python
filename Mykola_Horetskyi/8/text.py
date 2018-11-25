unassigned_cell_description = ["Unassigned cell, shouldn't be accessible by player"]

empty_cell_description = ["This room is empty",
"There is nothing in this room that's worth your attention.",
"Room is empty exept for some broken pieces of furniture and you.",
("You sense a movement and get ready for battle.\n"
"But it's just a starved rat that poses no threat,"
" maybe exept for some desiase."),
"This room is remarkebly unremarkable."]

entrance_cell_description = [("That's the place where you entered dungeon.\n"
"You hope you will be able to leave it as well.")]

treasure_description = ["You find treasure. You are rich!",
                      "You find a chest filled with gold"]

goblins_encounter = ["Suddenly a bunch of goblins rush at you from the shadows.",
("You sence a movement in front. A group small wretched green monsters "
"attempts to attack thinking that you're easy target.")]

goblins_fight = {
"melee":["They certainly chose the wrong target.",
"You hack goblins left and right with your sword."],

"magic":[("As you start cast your spells, spheres of fire materialize in "
"front of you and hurl themselves into enemy ranks."),
"You begin to chant the spell and see fear in you enemies' eyes."],

"guile":[("The goblins might me agile little basterds, but you are much more "
"agile and much more of a bastard. The first one to come at you gets a dagger "
"in the gut as you gracefully dodge his attack."),
("The might be superior in numbers, but you have superiority in everything else."
"Two goblins fall with knives in their throats and others start running:"
"some to you, some from you.")],

"other":["Goblins are definatly not your speciality."]}

goblins_survival = {
"melee":["Soon there is no one standing but you.",
"With all goblins dead or routed you remain victorious."],

"magic":[("As most of the goblins are now just piles of ash, "
"You're left alone tending to your wounds. Too bad healing magic isn't your"
"speciality.")],

"guile":[("While bleeding from several wounds you're still alive."
"That can't be said about your adversaries.")],

"other":[("With some luck on your side and a few casualties on enemy's "
"they rethink their decision to attack and hastly retreat.")]
}

goblins_defeat = {
"melee":["impossible"],

"magic":[("Magic is a great weapon, but fear is too. Seeing their comrades"
"burn to death the last few ramaining goblins, realizing that their lives"
"are forefit, mount an all out attack. As you lie on the ground bleeding to "
"deat you think you should've just scared them after all.")],

"guile":[("Even if for one of them to land a hit on you takes another three"
"dying by your hand, you still get hit. And bleed. And in the end..")],

"other":[("In the matter of moments you are surrounded and incapacicated."
"The goblins gloat at their easy victory.")]
}

hiden_blade_encounter = [("As you walk down the corridor a ruspy sound heard"
"right in front of you. A blade comes swinging from the hidden gap in the wall")]

hidden_blade_fight = {
"melee":["You try to block the blade with your sword."],

"magic":["You quickly cast a protection spell on yourself"],

"guile":["But this trap is no match for your sharp reflexes."],

"other":["The trap catches you off guard."]
}

hidden_blade_survival = {
"melee":[("You are partially successful as the blade just harms your shoulder "
"instead of decapitating you.")],

"magic":[("The spell does it's work. You are left wounded but certainly alive."
"Having powerup that completely protects you from harm is from the realm of "
"fairytales and games, not reality.")],

"guile":["The blade misses you, or rather you evade the blade."],

"other":[("You're so surprised by this that you trip and the blade misses you."
"Now it's the injury from falling you have to worry about.")]
}

hidden_blade_defeat = {
"melee":["The blade cuts your head off just as you've done to many of your enemies"],

"magic":["Too bad you can use protection spell only three times per day."],

"guile":["impossible"],

"other":["As expected the blade cuts you down."]
}

curse_encounter = [("Suddenly surroundings get even more darker even though it "
"would seem impossible and you hear a ghostly voice speaking in a language "
"long forgotten.")]

curse_fight = {
"melee":["You draw your sword and get ready to meet the owner of the voice."],

"magic":["You don't have to understand the voice to know that it's a curse."],

"guile":[("You can't kill and can't hide from the voice."
"It seems that you are out of options.")],

"other":[("You are scared and try to run, but the darkness and voice still "
"surround you.")]
}

curse_survival = {
"melee":[("You don't know if attacking darkness with your sword had any effect "
"besides raising your morale, but in the end you're alive "
"though feeling very sick.")],

"magic":[("Dealing with curses was your thesis in magic academy."
"You cast appropriate spell in 1.3 seconds after curse activating "
"and observe as darkness dissapears along with wailing voice.")],

"guile":[("It appears that besides other talents you're also packing some luck."
"As the voice stops you're left alive with weakness in all yor body.")],

"other":[("Though it might have seemed futile, running away gave some results."
"Either the source of the voice got tired of pursuing you or the curse itself "
"wasn't that deadly, the darkness and voice dissapeared leaving you "
"with minor injuries sustained during your hasty retreat. Or was it curse "
"of tripping over the rocks and accidently hitting random sharp objects?")]
}

curse_defeat = {
"magic":["impossible"],

"other":["You slowly succumb to the curse..."]
}

inquisition_encounter = ["You certainly didn't expect the Spanish Inqusition."]

inquisition_fight = {
"other":[("You are charged that you did on diverse dates commit heresy"
"against the Holy Church."),
("You informed of charges on four accounts: heresy by thought, "
"heresy by word, heresy by deed and heresy by action.")]
}

inquisition_survival = {
"other":[("You plead innocent but for no awail. You are fastened to the rack. "
"Luckily it seems that inquisitors are rather busy people very because after "
"giving the rack a few turns and poking you with soft cushions"
"they sat you in a comfy chair and hurry away to get another victim.")],

"none":[("You prepare for worse, but suddenly there is a sound of crossbeam "
"going out askew on treadle. As inquisitors go to investigate the source "
"of the sound you are left alone.")]
}

inqusition_defeat = {
"other":["Nobody escapes the Inquisition."]
}

enter_name_prompt = "Your name is.."

load_game_on_start_prompt = ("It seems there already exists adventurer with "
"that name. Is that you?(y/n)")

wrong_y_n_input = "Enter 'y' for yes, anything else for no."

new_game_start = ("While your country goes through economic recession, "
"you're fired from your job. With no money to pay for food or rent "
"you stumble on a notice informing about prospects of great fortunes "
"for people who would dare to explore dungeons. You immediately "
"set off to a local goverment administration for more details.")

administration = ("At administration minimum of your questions "
"are answered clearly and the only thing you understood is that you need "
"a special license in order to explore the dungeon. You're quite sure "
"that your country isn't Great Britain but keep your remarks to yourself "
"and hope you won't need a license for torch or flashlight.")

enter_proficiency_prompt = ("After spending your last money on license "
"you are surprised that exept for your name and address the only blanks"
"you have to fill is the one about your proficiency:\n"
"'Please specify if you have one of following proficiencies:\n"
"melee - you are proficient in close combat, if you are a former soldier, "
"that's one for you\n"
"magic - you specialize in arcane arts. For wizards and such.\n"
"guile - you are a cunning person with set of rather unscrupulous skills."
"A thief with good eye for heavy purse who can also snatch it without owner "
"noticing would be a fine example.\n"
"If no of specified three peoficiencies will be chosen then you will have none."
" You can choose no more than one proficiency. "
"This information will not be shared with judicial branch of goverment, "
"you can chose guile.")

enter_dungeon_width_prompt = ("After getting your license you're recieve "
"a rather impressive list of awailable dungeons. They come in many different "
"variations. Please specify width of your dungeon:")

enter_dungeon_height_prompt = ("Now you have to specify dungeon height, even "
"thought it's not vertical but just another horizontal dimention.")

go_to_dungeon = ["You go to the dungeon of your choosing."]

load_on_start = ["You wake up, remembering that you've beeen exploring dungeon.",
                   "You wake up after well deserved rest. Adventure awaits!"]

load_ingame = [("Suddenly you wake up, realizing that that all "
"that happened before was just a dream.")]

on_save_1 = ["You decide to take a break and fall asleep.",
"Feeling a little tired you fall asleep.",
"You take a nap."]

on_save_2 = ["Id doesn't last long and you wake up feeling uneasy.",
"Nothing disturbs as you dream of treasures and happy life.",
"You dream of something scary and wake up in cold sweat"]

on_no_save_file = ["You come to realization that this is only reality "
"that exists for you.",
 "No matter how you wish you were in other place right now, "
 "you have to face harsh reality."]

action_prompt = "You decide to:"

action_wrong = "You can't do that. You can hovewer:"

no_passage = ["You can't go there.",
"You carefully check the wall but there doesn't seem to be any passage.",
"There is just a wall in that direcion."]


adjacent_trap = ["You fell danger lurking nearby.",
"The passages leading from this room have an eerie feel about them."]

adjacent_treasure = ["You have a feeling in your gut that treasure is nearby.",
"Something tells you that the treasure is near."]

also = ["But that's not all.", "But there's also something else."]

end_map_description = "Here is the map of the dungeon."

play_again_prompt = "Would you like to play again?"

won = ["You can hardly can belive it, but it seems you've found all "
"treasure in this dungeon. The task of taking it back somehow doesn't seem hard at all."]

lost = ["YOU DIED"]

tell_position = "You enter the room with coordinates {},{}."

health_check = "You quickly assert your condition:"

health_description = {
0 : "You're dead.",
1 : "You're seriously injured.",
2 : "It's just a flesh wound.",
3 : "You're in perfect condition."
}

treasure_check = "You have {} treasures in your bag."

lets_end_this = ["You have had enough of this life!"]
