import random

die1 = random.randrange(1, 7)
die2 = random.randrange(1, 7)

if die1 + die1 == 7 or die1 + die1 == 11:
    print("you win!")
elif die1 + die1 == 2 or die1 + die1 == 3 or die1 + die1 == 12:
    print("craps")
else:
    newPoint = die1 + die2
    print("your new point: ",newPoint)
