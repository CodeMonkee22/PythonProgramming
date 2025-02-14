import random 

sum_probability = 0

for x in range(0,10):

    short_game = 0
    long_game = 0
    perfect_game = 0

    for y in range(0,100):
        turn = 1
        plank = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
        roll = 0

        print(plank)

        while True:
        
            for i in range(0,len(plank)):
                if plank[i] == 1:
                    person = i

            while(roll == 0):
                roll = random.randint(-3,3)

            plank[person] = 0

            person = person + roll

            if person < 0:
                person = 0
        
            elif person >= len(plank):
                person = len(plank)-1
            

            plank[person] = 1

            print(plank)


            if person == 0:
                print("You are back on the boat you have survived \n")
                if turn < 4:
                    short_game = short_game + 1
                elif turn > 14:
                    long_game = long_game + 1
                else:
                    perfect_game = perfect_game + 1
                break
            
            elif person == len(plank)-1:
                print("You fell off the boat, you have drowned \n")
                if turn < 4:
                    short_game = short_game + 1
                elif turn > 14:
                    long_game = long_game + 1
                else:
                    perfect_game = perfect_game + 1
                break   

            turn = turn + 1
            roll = 0

    sum_games = short_game + long_game + perfect_game


    print("Amount of perfect games is: {}".format(perfect_game))
    print("Amount of long games is: {} ".format(long_game))
    print("Amount of short games is: {} ".format(short_game))
    print("Sum of all games is: {} ".format(sum_games))

    probabilty_perfect_game = (perfect_game/sum_games)*100

    print("The probability for a perfect game is: {} \n".format(probabilty_perfect_game))
    sum_probability = sum_probability + probabilty_perfect_game

average_probability = sum_probability/10

print("The total probability for a perfect game is: {} ".format(average_probability))


