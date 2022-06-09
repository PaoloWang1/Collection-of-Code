import random

class Dice:
    def  __init__(self, num_faces):
        self.num_faces = int(num_faces)


    def roll(self):
        number = random.randint(1, self.num_faces)
        return number

dice1 = Dice(2)
dice2 = Dice(3)
dice3 = Dice(4)
dice4 = Dice(5)
dice5 = Dice(6)


while True:
    print(str(dice1.roll()) + "    " + str(dice2.roll()) + "    " +str(dice3.roll()) + "    " + str(dice4.roll()) + "    " +str(dice5.roll()))

    x = input("press enter to continue")

    if len(x):
        break
