import random
import time

totalPoint = 0
pointBalance= 1000

while True:
    print("------------------------------")
    userValue=int(input("please enter an integer value: "))
    
    if userValue <= pointBalance:
        print("craps game is starting...")
        time.sleep(1)
             
        die1 = random.randrange(1, 7)
        die2 = random.randrange(1, 7)
        
        

        if die1 + die2 == 7 or die1 + die2 == 11:
            oyunSonucu = True
            print("you win!")
        elif die1 + die2 == 2 or die1 + die2 == 3 or die1 + die2 == 12:
            oyunSonucu = False
            print("craps")
        else:
            oyunSonucu = True
            newPoint = die1 + die2
            print("your new point: ",newPoint)
            totalPoint = totalPoint + newPoint
            print("your total point: ",totalPoint)



        if oyunSonucu == True:
            pointBalance = pointBalance + 100
            print("your pointbalance: ",pointBalance)
        elif oyunSonucu == False:
            pointBalance = pointBalance - 100
            print("your pointbalance: ",pointBalance)


        if pointBalance == 0:
            print("Sorry, You busted!")

        elif pointBalance <= 500:
            print("Oh, you're going to lose, huh?")
        elif pointBalance <= 300:
            print("Aw c'mon, take a chance!")
        elif pointBalance <= 100:
            print("Don't forget! You're up big!")
    

    elif userValue > pointBalance:
        print("you entered an invalid value")

    else:
        print("error")

    print("------------------------------")