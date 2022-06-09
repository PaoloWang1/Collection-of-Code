a = [1, 23, 432, 14, 412, 5, 21, 5, 32, 321, 32, 1, 412, 3]
greatest = 0
smallest = 0
for num in (1, len(a) + 1):
    if (a[num] > greatest):
        greatest = a[num]
    if (a[num] < smallest):
        smallest = a[num]
print("The greatest number was ", greatest)
print("The smallest number was ", smallest)
    
