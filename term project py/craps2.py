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

        die1 = random.randrange(1,7)
        die2 = random.randrange(1,7)
        total = die1 + die2
        print("Player rolled {}" .format(total))


        if total == 7 or total == 11:
            game_status = "WON"

        elif total == 2 or total == 3 or total == 12:
            game_status = "LOST"

        else:
            game_status = "Continue"

        point = total
        print ("Point is {}".format(point))


        while game_status == "Continue":
            sum = total
    
        if sum == point:            #Win by 'making point' 
            game_status = "WON" 
        elif sum == 7:                 #Lose by rolling a 7
            ame_status = "LOST"

        #Keep rolling    

        
        if game_status == "WON":
            print("Player wins!")
        else:
            print("Player loses....") 






