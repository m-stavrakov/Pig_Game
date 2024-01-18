import random

# Rolling the dice
def roll_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll
    
# Players
# while True:
    # players = input("Enter the number of players (2-4): ")
    # Checking if the the user entered the right number of players 
    # isdigit is telling us if the value is a whole number
    # if players.isdigit():
        # players = int(players)
        # if 2 <= players <= 4:
            # break
        # else:
            # print("Must be between 2 - 4 players.")
    # else:
        # print("Invalid, try again")

# max_score = 50

def play_turn():
    current_score = 0

    while True:
        should_roll = input("Would you like to roll (y)? ")

        if should_roll.lower() != 'y':
            break

        value = roll_dice()
        print("You rolled a:", value)

        if value == 1:
            print("You rolled a 1! Turn done!")
            current_score = 0
            break
        else:
            current_score += value
            print("Your current score is:", current_score)

    return current_score
        

def play_game(players, max_score=50):
    # Will contain the scores of the players
    player_scores = [0 for _ in range(players)] # the _ is replacing the variable (i); teh 0 will represent the number of players if we have 3 players that would be 3 0s

    # Stopping the game when max_score is reached
    while max(player_scores) < max_score:

        for player_inx in range(players):
            print("\nPlayer number", player_inx + 1, "Turn has just started!")
            print("Your total score is:", player_scores[player_inx], "\n")
            
            current_score = play_turn()
            player_scores[player_inx] += current_score
            
            print("Your total score is:", player_scores[player_inx])

            if player_scores[player_inx] >= max_score:
                print("Player", player_inx + 1, "wins!")
                return player_inx + 1

    # Finding the winner
    # max_score = max(player_scores)
    # winning_inx = player_scores.index(max_score)
    # print("Player number", winning_inx + 1, "is the winner with a score of:", max_score)

    # return max(player_scores), player_scores.index(max(player_scores)) + 1

