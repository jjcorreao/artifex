
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

class VPlot:

    def __init__(self, *args, **kwargs):
        path = args[0]
        self.x = kwargs.get('x')
        self.y = kwargs.get('y')
        self.Lx = kwargs.get('Lx')
        self.m1 = kwargs.get('m1')
        self.g = kwargs.get('g')

        # self.calc_xy()
        self.calc_length()
        self.tension()

    def calc_xy(self):
        # Image.rea
        # self.x = None
        # self.y = None
        pass

    def calc_length(self):
        self.L1 = np.sqrt(self.x**2 + self.y**2)
        self.L2 = np.sqrt((self.Lx-self.x)**2 + self.y**2)
        self.alpha = np.arcsin(self.y/self.L1)
        self.beta = np.arcsin((self.L1/self.L2)*np.sin(self.alpha))

    def tension(self):
        self.T2 = (self.m1*self.g*np.cos(self.alpha))/(np.sin(self.beta)*(np.cos(self.beta)+np.cos(self.alpha)))
        self.T1 = (self.T2*np.cos(self.beta))/np.cos(self.alpha)

