#Multiple line graphs: Using matplotlib, we can plot multiple lines on the same graph.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([12, 44, 65, 88])

plt.plot(x, y1, marker="v",
         markersize = 30,
            markerfacecolor= '#32fa67',
            markeredgecolor= '#15e2ed',
            linestyle= 'dashdot',
            linewidth= 3,
            color= '#eb8a0c')

plt.plot(x, y2, marker="o",
         markersize = 30,   
            markerfacecolor= '#f0f0f0',
            markeredgecolor= '#15e2ed',
            linestyle= 'dotted',
            linewidth= 3,
            color= '#eb8a0c')


plt.show()

