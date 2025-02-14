import random

sum_wins = 0

for x in range(0,100):
    print("New promotion \n")
    weeks = 0
    coupon_array = [0, 0, 0, 0, 0, 0]

    
    while(weeks < 26):

        x = random.randint(0,5)

        for i in coupon_array:
            coupon_array[x] = 1

        print("Values if coupons have been found \n {} \n".format(coupon_array))

        if coupon_array.count(1) == 6:
            print("You have won the coupon festival \n Thank you for participating \n")
            sum_wins += 1
            break

        weeks = weeks + 1

probability_wins = sum_wins
    
print("The probability to win the prize is {}%".format(probability_wins))
