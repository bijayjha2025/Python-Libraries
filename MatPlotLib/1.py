#Pyplot is a collection of functions that make Matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

import matplotlib.pyplot as plt
import numpy as np

x= np.array([2023, 2024, 2025, 2026, 2027])
y= np.array([12,44,65,88,90])

plt.plot(x,y)
plt.show()

