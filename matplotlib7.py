import numpy as np
from matplotlib import pyplot as plt
x = np.arange(1,6)
print(x)
y1 = 3*x
y2 = (x*2)-2
print(y1)
print(y2)
plt.title("Two Line Plot using Matplatlib")
plt.xlabel('x axies')
plt.ylabel('y axies')
plt.subplot(2,1,1)
plt.plot(x,y1,color='g', linestyle='-',linewidth=1)
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(x,y2,color='r', linestyle='-',linewidth=1)
plt.grid(True)
plt.show()