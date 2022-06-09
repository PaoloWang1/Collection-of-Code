import numpy as np

list1 = np.ones((25))
list1[::2] = 0
list1 = list1.reshape(5,5)
print(list1)
