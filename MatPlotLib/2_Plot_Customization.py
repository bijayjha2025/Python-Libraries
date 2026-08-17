#Plot Customization: Using matplotlob, we can customize various components of a graph.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y = np.array([15, 25, 30, 20])

plt.plot(x, y, marker="v",
         markersize = 30,
         markerfacecolor= '#32fa67',
         markeredgecolor= '#15e2ed',
         linestyle= 'dashdot',
         linewidth= 3,
         color= '#eb8a0c')

#Using marker as different things like *, ., o, v, and many more. Visit matplotlib.markers for more

#we can also set markersize as per our need

#markerfacecolor is used to set the color of the marker

#markeredgecolor is used to set the color of the edge of the marker

#linestyle is used to set the style of the line. It can be solid, dashed, dashdot, dotted, etc.

#linewidth is used to set the width of the line.

#color is used to set the color of the line whereas markerfacecolor is used to set the color of the marker.

plt.show()