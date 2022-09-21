import numpy as np
from matplotlib import pyplot as plt
x = np.arange(1,20)
print(x)
y = 2*(x-2)
print(y)

plt.plot(x,y)
plt.title("Line Plot using Matplatlib")
plt.xlabel('x value')
plt.ylabel('y=2*(x-2)')
plt.show()
