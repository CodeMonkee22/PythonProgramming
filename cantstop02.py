import random

# Intialise the amount of advances, amount of busts in the game 
# & the total amount of rolls.
advance_count = 0
bust_count = 0
total_rolls = 0

# For loop to iterate a certain amount of times to roll and
# check the value of each die.
for i in range(0,10000):
    print("New Roll \n")
    total_rolls += 1  # Add one to total amount of rolls.
    dice = [0,0,0,0]  # Intialise dice array.

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

    # Check if one pair is the value sum of 2, 4, 11 and add to the advance count.
    if AB_Sum == 2 or CD_Sum == 2 or AC_Sum == 2 or BC_Sum == 2 or AD_Sum == 2 or BD_Sum == 2:
        print("You got a correct number, you can now advance \n")
        advance_count += 1

    elif AB_Sum == 4 or CD_Sum == 4 or AC_Sum == 4 or BC_Sum == 4 or AD_Sum == 4 or BD_Sum == 4:
        print("You got a correct number, you can now advance \n")
        advance_count += 1
    
    elif AB_Sum == 11 or CD_Sum == 11 or AC_Sum == 11 or BC_Sum == 11 or AD_Sum == 11 or BD_Sum == 11:
        print("You got a correct number, you can now advance \n")
        advance_count += 1
    
    # If none of the sums equal 3,8,11 add to the bust count
    else:
        print("You got no numbers, you are bust \n")
        bust_count += 1

# Calculate the probability of both advance and bust.
probabilty_advance = (advance_count/total_rolls)*100
probability_bust = (bust_count/total_rolls)*100

# Print the probability of both advance and bust.
print("The chance of advancing on the board is {}% \n".format(probabilty_advance))
print("The chance of being bust is {}% \n".format(probability_bust))
