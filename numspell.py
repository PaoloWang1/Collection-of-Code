def numspell(num):
    printed = ""
    units = ["", "one", "two", "three", "four","five", "six", "seven","eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen","sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["","", "twenty", "thirty", "forty", "fifty","sixty","seventy","eighty","ninety"]
    if (num < 0):
        printed += "negative "
        num = num * -1
    if (num < 20):
        printed = units[num]
    elif (num < 100):           
        for num1 in range(3,11):
            if (num < num1*10):
                printed += tens[num1-1] +"-"+ units[num-(num1-1)*10]
                break
    else:
        for hundreds in range(1,11):
            if (num < hundreds * 100):
                printed += units[hundreds-1] + " hundred "
                num = num - ((hundreds - 1)*100)
                if (num < 20):
                    printed += "and " + units[num]
                    break
                else:
                    for num1 in range(3,11):
                        if (num < num1*10):
                            printed += tens[num1-1] +"-"+ units[num-(num1-1)*10]
                            break
                break
    print(printed)
spell = int(input("Enter a number: "))
numspell(spell)
    
    
        
    
    
    
    
        
