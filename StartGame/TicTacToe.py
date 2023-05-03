from Options import TwoPlayers
from Options import Branches

from IPython.display import clear_output

def tic_tac_toe():
	print('\nWelcome to the game of Tic-Tac-Toe!\n')
	option = choose_option()
	if option == 1:
		TwoPlayers.two_players()
	else:
		Branches.ai_operated()

def choose_option():
	list1 = ['1','one','ONE','One','OnE','oNe','oNE','ONe']
	list2 = ['2','two','TWO','Two','TwO','tWo','tWO','TWo']
	print('\nGame options :-')
	print('\n   1. Play a two-player game.')
	print('\n   2. Play against Jared, the AI-powered futuristic bot.')
	option = input('\nChoose an option:  \n\n')
	while option not in list1 and option not in list2:
		print('\nEnter a valid option...')
		option = input('\nChoose an option between 1 and 2:  \n\n')
	if option in list1:
		return 1
	else:
		return 2