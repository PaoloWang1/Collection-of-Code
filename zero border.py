import numpy as np

fives = np.zeros(25)
fives[::1] = 5
fives = fives.reshape(5,5)

for x in range(2):
    fives[0][::1]=0
    fives[4][::1]=0
    fives = np.transpose(fives)

print(fives)
