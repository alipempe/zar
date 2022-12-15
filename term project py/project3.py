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

        def diceRoll():
            die1 = random.randrange(1, 7)
            die2 = random.randrange(1, 7)
            sumofDie = die1 + die2

            return sumofDie


        #First dice roll  
        sum = diceRoll()    

        if sum == 7 or sum == 11:
            oyunSonucu = "win"
            print("you win!")
        elif sum == 2 or sum == 3 or sum == 12:
            oyunSonucu = "lost"
            print("craps")
        else:
            oyunSonucu = "continue"
            newPoint = sum
            print("your new point: ",newPoint)
            totalPoint = totalPoint + newPoint
            print("your total point: ",totalPoint)


        #Keep rolling   
        while oyunSonucu == "continue":
            sum = diceRoll()
    
            if sum == newPoint:            #Win by 'making point' 
                oyunSonucu = "win" 
            elif sum == 7:                 #Lose by rolling a 7
                oyunSonucu = "lost"


        if oyunSonucu == "win":
            pointBalance = pointBalance + userValue
            print("your pointbalance: ",pointBalance)
        elif oyunSonucu == "lost":
            pointBalance = pointBalance - userValue
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