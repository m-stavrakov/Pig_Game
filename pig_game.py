import random

# Rolling the dice
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

# Players
while True:
    players = input("Enter the number of players (2-4): ")
    # Checking if the the user entered the right number of players 
    # isdigit is telling us if the value is a whole number
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again")

max_score = 50

# Will contain the scores of the players
player_scores = [0 for _ in range(players)] # the _ is replacing the variable (i); teh 0 will represent the number of players if we have 3 players that would be 3 0s

# Stopping the game when max_score is reached
while max(player_scores) < max_score:
    
    for player_inx in range(players):
    
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)? ")
            
            if should_roll.lower() != 'y':
                break
            
            value = roll()
            if value == 1:
                print("You rolled 1! Turn done!")
                break
            else:
                current_score += value
                print("You rolled a: ", value)
                
            print("Your score is: ", current_score)
    
        player_scores[player_inx]
