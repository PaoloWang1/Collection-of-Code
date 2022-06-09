def count_letter(string, letter):
    count = 0
    for x in str(string):
        if str(letter) == x:
            count +=1
    print(count)
    
