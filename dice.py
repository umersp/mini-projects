import random

list = [1 , 2 , 3,4,6]
x = input("Press ' R ' to roll the Dice : ")

if x == "R":
    # print(random.randint(1,6))
    print(random.choice(list))