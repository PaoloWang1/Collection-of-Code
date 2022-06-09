lista = [1,2,3,4,4,6,7,8,9]
yesorno = 0
num2 = lista[0]
for num in lista:
    if num2 == num:
        num2 = num2 + 1
        yesorno = 1
    else:
        yesorno = 0
if yesorno == 1:
    print("The list is in order")
else:
    print("The list is not in order.")
