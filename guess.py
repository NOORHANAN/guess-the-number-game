import random
jackpot = random.randint(1,100)
guess = int(input("Enter the number"))
counter=1
while guess != jackpot:
        if guess < jackpot:
                print("guess higher")
        else:
                print("guess lower")
        guess= int(input("Enter the number"))
        counter+=1
print("Right you have got the prize in ", counter)
