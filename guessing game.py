import random
rand = random.randint(1, 100)
num = int(input("Guess what my integer from 1 to 100 is: "))
while(num != rand):
    if (num > rand):
        print("Your number is too high.")
        num = int(input("Guess what my integer from 1 to 100 is: "))
    if(num < rand):
        print("Your number is too low.")
        num = int(input("Guess what my integer from 1 to 100 is: "))
print("You guessed my number! Nice Job!")
