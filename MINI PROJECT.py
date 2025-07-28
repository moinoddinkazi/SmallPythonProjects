


import math
import time
import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from numpy.lib import flip
initial_time = time.time()
h=50
h1 = h/2
a1 = math.sqrt(3)/2
x=np.array([0,h1-a1*h1, h1/2,h1,h1+(h1/2),a1*h1+h1,h])
theta1=linspace(0,120,7)
theta2=linspace(180,270,7)
fig = plt.subplots (figsize=(20, 8))
plt.grid(True)
plt.xlabel('Theta')
plt.ylabel('Lift')
plt.xticks(np.arange(0, 280, step=10))
plt.yticks (np.arange(0, 55, step=2))
plt.plot(theta1,x, theta2, flip(x))
print("Time Required To Draw Curve using Python Code: ",time.time()-initial_time,"Seconds")
plt.show()