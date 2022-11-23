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
        self.fig, self.ax = plt.subplots()

    """
        Setup the matplot graph
    """
    def initPlot(self):
        #self.fig, self.ax = plt.subplots()
        self.ax.set_title('Vertical Clamp Analysis')
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(-4, 8)

    """
        Draw the plunger part
    """
    def drawPlunger(self):
        for i in range(len(self.plunger_x_cords)):
            plt.plot(self.plunger_x_cords[i], self.plunger_y_cords[i], color='red', linestyle="--")

    """
        Draw the lever in locked position
    """
    def drawLever(self, frame_number):
        x_cords = []

        for val in self.lever_x_cords:
            x_cords.append(val + (frame_number * 0.1))
        
        plt.plot(x_cords, self.lever_y_cords, color='blue', linestyle="--")

    """
        Animation callback method
    """
    def anim(self, frame_number):
        self.ax.clear()
        self.initPlot()
        self.drawLever(frame_number)
        self.drawPlunger()

    """
        Run the main analysis 
    """
    def run(self, animate=False):
        if animate == True:
            anim = animation.FuncAnimation(self.fig, self.anim, frames=5, blit=False, repeat=True, interval=100)    
            plt.show()
            return
        
        self.initPlot()
        self.drawPlunger()
        self.drawLever()
        self.drawLeverUnlocked()
        plt.show()

    """
        Draw the lever in unlocked position
    """
    def drawLeverUnlocked(self):
        unlocked_lever_x = np.sin(45 * np.pi / 180) * 3
        x_cords = [unlocked_lever_x]
        y_cords = [unlocked_lever_x]

        for i in range(2):
            unlocked_lever_x += 0.7
            x_cords.append(unlocked_lever_x)
            y_cords.append(unlocked_lever_x)
        
        print(f'x: {x_cords}\ny: {y_cords}')
        plt.plot(x_cords, y_cords, color='black', linestyle="--")

        # increase x and decrease y
        x_cords = [unlocked_lever_x + .6, unlocked_lever_x + 1.02]   
        y_cords = [y_cords[2], y_cords[2]]

        plt.plot(x_cords, y_cords, color='black', linestyle="--")


if __name__ == '__main__':
    vs = VertCam()
    vs.run(animate=True)
    