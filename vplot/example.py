__author__ = 'pytthon'

import os
os.sys.path.append("/Users/pytthon/Projects/v-plotter/")

from vplot import plotter

path = "/Users/pytthon/Projects/v-plotter/vplot/data/Lenna.png"
plotr = plotter.VPlot(path, Lx = 1.5, x = 0.1, y = 0.5, m1 = 5, g = 1)

import matplotlib.pyplot as plt

from skimage import data, io
from skimage.filters import threshold_otsu, threshold_adaptive


