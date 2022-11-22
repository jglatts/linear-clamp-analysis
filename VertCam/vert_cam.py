import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from matplotlib import rc

class VertCam:

    """
        VertCam constructor
    """
    def __init__(self):
        self.plunger_x_cords = [[1, 2], [2, 3, 4], [4, 3, 2, 1], [1, 1, 1]]
        self.plunger_y_cords = [[2, 2], [2, 1, 0], [0, 0, 0, 0], [0, 1, 2]]
        self.lever_x_cords = [1.5, 1.5, 1.5]
        self.lever_y_cords = [2, 3, 4]

    """
        Setup the matplot graph
    """
    def initPlot(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Golf Path Sim')
        self.ax.set_xlim(0, 5)
        self.ax.set_ylim(-4, 5)

    """
        Draw the plunger part
    """
    def drawPlunger(self):
        for i in range(len(self.plunger_x_cords)):
            plt.plot(self.plunger_x_cords[i], self.plunger_y_cords[i], color='r', linestyle="--")

    """
        Draw the lever part
    """
    def drawLever(self):
        plt.plot(self.lever_x_cords, self.lever_y_cords, color='blue', linestyle="--")

    """
        Run the main analysis 
    """
    def run(self):
        self.initPlot()
        self.drawPlunger()
        self.drawLever()
        plt.show()



if __name__ == '__main__':
    vs = VertCam()
    vs.run()
    