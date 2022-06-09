greatest = 0
def factor(num):
    for fac in range(1, num):
        if (num % fac == 0):
            greatest = fac
    print(greatest)
ainput = int(input("Enter a number: "))
factor(ainput)
            
        
    
