import numpy as np
from matplotlib import pyplot as plt
x = np.arange(1,11)
print(x)
y = 2*x
print(y)
plt.plot(x,y,color='r', linestyle=':',linewidth=5)
plt.show()