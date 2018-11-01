from random import choice


def generate_bots(n):
	players = {f'bot{i}' : 0 for i in range(n)}
	
	return players


def inp_player_weapon():

	player_weapon = ''

	global WEAPONS
	WEAPONS = {3 : 'rock', 2 : 'scissors', 1 : 'paper'}

	while not player_weapon in WEAPONS.values():
		player_weapon = input('Enter your answer: ')
		
	return list(WEAPONS.keys())[list(WEAPONS.values()).index(player_weapon)]
		

players_amount = ''
while not players_amount.isdigit():
	players_amount = input('Enter players quantity: ')
	
players_amount = int(players_amount)

bots = generate_bots(players_amount - 1)
losers = []

player_in_game = True

while players_amount > 1:
	if player_in_game:
		player_response = inp_player_weapon()
	
	bots = { k: choice([1,2,3]) for k,v in bots.items() }

	print(f'\nyou: {WEAPONS[player_response]}')
	to_print = [f'{key}: {WEAPONS[value]}'for key, value in bots.items()]
	print('\n'.join(to_print), '\n')
	
	players_responses = list(bots.values())
	players_responses.append(player_response)
	
	responses_types_counts = {i : players_responses.count(i) for i in players_responses}

	if len(responses_types_counts) == 2:
		responses_types = list(responses_types_counts.keys())
		responses_types.sort()

		if responses_types == [1,3]:
			lose_response = 3

		else:
			lose_response = min(responses_types)

		if player_response == lose_response and player_in_game:

			losers.append('you')
			player_in_game = False

		losers.extend([ k for k,v in bots.items() if v == lose_response])
	
		bots = {k : v for k,v in bots.items() if k not in losers}

		print('bots', bots)
		print('losers', losers)

		players_amount = len(bots) + int(player_in_game)
	

losers.reverse()

to_print = []

bots_left = list(bots.keys())
print(bots_left)

if player_in_game:
	to_print.append('You won!')
	to_print.extend('1. You')
	to_print.extend([f'{i + 1}. {bots_left[i]}' for i in range(len(bots_left))])
	to_print.extend([f'{i + len(bots_left) + 1}. {losers[i]}' for i in range(len(losers))])
else:
	to_print.extend([f'{i + 1}. {bots_left[i]}' for i in range(len(bots_left))])
	to_print.extend([f'{i + len(bots_left) + 1}. {losers[i]}' for i in range(len(losers))])

print('Leaderboard\n','\n'.join(to_print))
