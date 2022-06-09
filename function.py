quit = "n"
while (quit == "n"):
    x=input("Please enter the value of x: ")
    x = float(x)
    y = (2*x**2-5*x+2)
    y = str(y)
    print("The value of y is: " + y)
    quit = input("Would you like to quit? (y/n): ")
    quit = str(quit)
