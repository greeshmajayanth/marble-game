Programming language used: Python 3.10.6

Code structure:

red_blue_nim.py - contains the main program containing functions:
game_over_check - checks if the game is over 
calculate_score - calculates the score 
computer_move - computer makes a move based on minimax algorithm 
minMax - Mini-max algorithm function with alpha-beta prunig
evaluate - defines the evaluation function for mini-max algorithm
human_move - reduces a marble from the pile mentioned by the user
game_over_check - loop to navigate the players turns

eval_fuction.txt - explains the eval function chosen for this program

How to run the code:
Run the command - 'python red_blue_nim.py <num-red> <num-blue> <first-player> <depth>'
first-player can be computer or human
Example - 'python red_blue_nim.py 5 4 computer 3'