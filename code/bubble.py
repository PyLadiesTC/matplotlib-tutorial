"""
Example of matplotlib colormaps
http://matplotlib.org/api/colors_api.html
"""
import file_handler
import numpy as np

import matplotlib
from matplotlib import figure
from matplotlib.backends.backend_agg import (
FigureCanvasAgg as FigureCanvas)

import matplotlib.cm as mcm
import matplotlib.colors as mcolors

a = np.random.permutation(np.arange(10))
b = np.random.permutation(np.arange(10))
c = np.random.permutation(np.arange(10))
d = np.random.permutation(np.arange(0,10))

fig = figure.Figure()

canvas = FigureCanvas(fig)
cmap = mcm.spring
norm = mcolors.BoundaryNorm(np.arange(11), cmap.N)

ax = fig.add_subplot(1,1,1)
scat = ax.scatter(a,b,c=c, s=(d+10)*50,
                  cmap=cmap,norm=norm)
fig.colorbar(scat, ax=ax, fraction=.45)

image_name = "cmapbubble.png"
file_name = file_handler.get_file_name(image_name)
with open (file_name, 'w') as f:
    canvas.print_figure(f,
        facecolor='lightgray')
