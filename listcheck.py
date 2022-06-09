a = [1,2,3,4,5,]
b = [2,4,1,35,5]
for num in range(1, len(a) + 1):
    if a[num] != b[num]:
        print("The lists are different.")
        quit()
    
