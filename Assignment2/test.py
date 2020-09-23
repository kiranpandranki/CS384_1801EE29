import numpy as np
import tutorial02 as tut
x, y = np.loadtxt("results.csv", delimiter=",",
                  usecols=(0, 1), unpack=True, skiprows=1)
x = list(x)
y = list(y)
print(tut.median(x))
print(tut.mse(x, y))
