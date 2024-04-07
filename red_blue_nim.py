import sys

red_marbles  = int(sys.argv[1])                #Get the number of red marbles
blue_marbles = int(sys.argv[2])                #Get the number of blue marbles
first_player = str(sys.argv[3])                #Get the first player
depth_limit  = int(sys.argv[4])                #Get the depth

#function to check if the game is over
def game_over_check():
    return red_marbles == 0 or blue_marbles == 0

#function to calculate the score
def calculate_score():
    return 2 * red_marbles + 3 * blue_marbles

#function for the computer to make a move using the minMax algorithm
def computer_move():
    print("Computer's turn:")
    global red_marbles, blue_marbles
    pile, value = minMax(depth_limit, float('-inf'), float('+inf'), True)
    if pile == "red":
        print("Computer removes a red marble.")
        print("Eval value:", value)
        red_marbles -= 1
    else:
        print("Computer removes a blue marble.")
        print("Eval value:", value)
        blue_marbles -= 1
    print("Remaining red marbles:", red_marbles)
    print("Remaining blue marbles:", blue_marbles)

#function for computer to determine the best move using minimax algorithm with alpha-beta pruning and depth mentioned by the user
def minMax(depth, alpha, beta, max_player):
    global red_marbles, blue_marbles
    if depth == 0 or game_over_check():
        return None, evaluate(max_player)

    if max_player:
        max_value = float('-inf')
        best_action = None
        for pile in ["red", "blue"]:
            if pile == "red" and red_marbles == 0:
                continue
            elif pile == "blue" and blue_marbles == 0:
                continue

            if pile == "red":
                red_marbles -= 1
            else:
                blue_marbles -= 1

            value = minMax(depth - 1, alpha, beta, False)[1]

            if pile == "red":
                red_marbles += 1
            else:
                blue_marbles += 1

            if value > max_value:
                max_value = value
                best_action = pile

            alpha = max(alpha, max_value)
            if beta <= alpha:
                break

        return best_action, max_value
    else:
        min_value = float('+inf')
        best_action = None
        for pile in ["red", "blue"]:
            if pile == "red" and red_marbles == 0:
                continue
            elif pile == "blue" and blue_marbles == 0:
                continue

            if pile == "red":
                red_marbles -= 1
            else:
                blue_marbles -= 1

            value = minMax(depth - 1, alpha, beta, True)[1]

            if pile == "red":
                red_marbles += 1
            else:
                blue_marbles += 1

            if value < min_value:
                min_value = value
                best_action = pile

            beta = min(beta, min_value)
            if beta <= alpha:
                break

        return best_action, min_value
    
#Evaluation function
def evaluate(max_player):
    if max_player:
        if red_marbles > blue_marbles:
            return 20  # max player has more red marbles
        else:
            return 30  # max player has more blue marbles
    else:
        if red_marbles > blue_marbles:
            return -20  # min player has more red marbles
        else:
            return -30  # min player has more blue marbles

#function for the human's turn
def human_move():
    print("Your turn:")
    # ask the user to select a pile 
    pile = input("Select a pile (red or blue): ")
    if pile == "red":
        print("You remove a red marble.")
        global red_marbles
        red_marbles -= 1
    else:
        print("You remove a blue marble.")
        global blue_marbles
        blue_marbles -= 1
    print("Remaining red marbles:", red_marbles)
    print("Remaining blue marbles:", blue_marbles)

#main game loop
while not game_over_check():
    
    if first_player == "computer":
        #computer's turn
        computer_move()
        
        if game_over_check():
            print("Game over")
            score = calculate_score()
            print("You won with " + str(score) + " points")
            break
            
        #human turn
        human_move()

        if game_over_check():
            print("Game over")
            score = calculate_score()
            print("Computer won with " + str(score) + " points")
            break

    elif first_player == "human":
        #human's turn
        human_move()
        
        if game_over_check():
            print("Game over")
            score = calculate_score()
            print("Computer won with " + str(score) + " points")
            break
            
        #computer's turn
        computer_move()

        if game_over_check():
            print("Game over")
            score = calculate_score()
            print("You won with " + str(score) + " points")
            break



