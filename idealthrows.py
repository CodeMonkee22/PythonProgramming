import random

# Intialise all throw variables and total amount of games variable.
one_roll = 0
two_rolls = 0
three_rolls = 0
four_rolls = 0
more_rolls = 0
total_games = 0

# For loop to iterate each game of Can't Stop to certain number of games.
for i in range(0,10000):
    print("New Game")
    game = True  # Make each start of game true 
    rolls = 1     # Start the rolls counter
    total_games += 1  # Add one to the total games

    # While loop for each game played until bust.
    while(game == True):
        print("New Roll")
        dice = [0,0,0,0] # Intialise dice array.
    
        # Randomly roll four dice.
        for j in range(0,4):
            dice[j] = random.randint(1,6)
        
        print("values of all dice are {} ".format(dice))

        # Sum all paired combinations of all four dice.
        AB_Sum = dice[0] + dice[1]
        CD_Sum = dice[2] + dice[3]
        AC_Sum = dice[0] + dice[2]
        BD_Sum = dice[1] + dice[3]
        AD_Sum = dice[0] + dice[3]
        BC_Sum = dice[1] + dice[2]

        print("The throw turn is {}".format(rolls))

        # Check if one pair is the value sum of 3, 8, 11 and add another turn as you have advanced.
        if AB_Sum == 3 or CD_Sum == 3 or AC_Sum == 3 or BC_Sum == 3 or AD_Sum == 3 or BD_Sum == 3:
            print("You got a correct number, you can now advance \n")
            rolls+=1

        elif AB_Sum == 8 or CD_Sum == 8 or AC_Sum == 8 or BC_Sum == 8 or AD_Sum == 8 or BD_Sum == 8:
            print("You got a correct number, you can now advance \n")
            rolls+=1
        
        elif AB_Sum == 11 or CD_Sum == 11 or AC_Sum == 11 or BC_Sum == 11 or AD_Sum == 11 or BD_Sum == 11:
            print("You got a correct number, you can now advance \n")
            rolls+=1
        
        # Else check what number of rolls before bust and add that to it's counter then exits the game.  
        else:
            print("You got no numbers, you are bust \n")
            if rolls == 1:
                one_roll+=1
            elif rolls == 2:
                two_rolls+=1
            elif rolls == 3:
                three_rolls+=1
            elif rolls == 4:
                four_rolls+=1
            else:
                more_rolls+=1
            game = False
    


# Calculate the probability of each number of throws before bust. 
probabilty_one = (one_roll/total_games)*100
probability_two = (two_rolls/total_games)*100
probability_three = (three_rolls/total_games)*100
probability_four = (four_rolls/total_games)*100
probability_more = (more_rolls/total_games)*100

# Print the probability of each number of throws before bust. 
print("The chance of there being one throw before bust is: {}% \n".format(probabilty_one))
print("The chance of there being two throws before bust is: {}% \n".format(probability_two))
print("The chance of there being three throws before bust is: {}% \n".format(probability_three))
print("The chance of there being four throws before bust is {}% \n".format(probability_four))
print("The chance of there being more than four throws before bust is {}% \n".format(probability_more))