import numpy as np
from matplotlib import pyplot as plt
student = {'Adity':34,'Rabia':1,'Akib':22,'Sharif':27}
name = student.keys()
print(name)
roll = student.values()
print(roll)
plt.bar(name,roll)
plt.show()