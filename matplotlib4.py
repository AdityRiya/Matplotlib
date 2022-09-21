import numpy as np
from matplotlib import pyplot as plt
x = np.arange(1,11)
print(x)
y1 = 2*x
y2 = (x-1)
print(y1)
print(y2)
plt.title("Two Line Plot using Matplatlib")
plt.xlabel('x axies')
plt.ylabel('y axies')
plt.plot(x,y1,color='g', linestyle='-',linewidth=4)
plt.plot(x,y2,color='r', linestyle='-',linewidth=4)
plt.show()