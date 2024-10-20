#  Interpolation

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(11)
y=np.array([2.0, 1.9, 1.7, 1.5, 0.5, 0.0, 0.8, 2.0, 0.9, 0.2, 2.0])

plt.plot(x,y,"o:")
# plt.show()


from scipy.interpolate import interp1d

#  Linear # Nearest  # Zero # SLinear # Quadratic # Cubic

Predict= interp1d(x,y,kind="cubic")

x2=np.linspace(0,10,100)
y2=np.array([Predict(x)for x in x2])

plt.plot(x2,y2,"ro:")


print(f"x:1.5,y:{Predict(1.5)}")
plt.show()