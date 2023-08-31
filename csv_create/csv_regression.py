import numpy as np
import matplotlib.pylab as plt

X=2*np.random.rand(100,1)
y=4+3*X+np.random.rand(100,1)
plt.scatter(X,y)
plt.xlabel("X")
plt.ylabel("y")
plt.show()
