value = float(input("What is the value of your car: "))
age = float(

    input("What is your age: "))
tickets = float(input("How many tickets have you gotten: "))
premiumb = 0.05 * value
premiuma = premiumb
if (age < 25):
    premiuma = premiumb * 1.15
elif (age < 30):
    premiuma = premiumb * 1.1
if (tickets == 1):
    premiuma = premiuma + 1.1 * premiumb
elif (tickets == 2):
    premiuma = premiuma + 1.25 * premiumb
elif (tickets == 3):
    premiuma = premiuma + 1.5 * premiumb
elif (tickets > 3):
    print("You have too many tickets!")
    quit()
print("Premium is: $" + str(premiuma))
#The base premium is 5 percent of the value of the car.
#2. Drivers under 25 years old pay 15 percent more and drivers from 25
#through 29 pay 10 percent more from the base premium.
#3. A driver with one traffic ticket pays 10 percent over the base premium
#already figured. Two tickets draws a 25 percent extra charge; three tickets
#adds 50 percent; and drivers with more than three tickets are refused
#coverage
