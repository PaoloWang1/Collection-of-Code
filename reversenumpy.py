import numpy as np

original = np.arange(1,26)
original = original.reshape(5,5)

new = original.reshape(1, 25)
new = new[0][::-1]
new = new.reshape(5,5)
print(new)
