turns = 5
word = "words"

while turns > 0:
    guess = input("Enter a character: ")
    for a in len(words):
        if guess in words:
            
