
def factorial(num):
    fact = 1
    for factors in range(1, num + 1):
        fact = fact * factors
    print(fact)
parameter = int(input("Enter a number: "))
factorial(parameter)

        
