# Design analysis for a linear toggle clamp 
# Inspired by https://www.instructables.com/The-Linear-Toggle-Clamp/
import numpy as np
import matplotlib.pyplot as plt

def calcPts(theta, lhandle, lpivot, lbar):
    t = theta * np.pi/180
    xhandle = lhandle * np.sin(t)
    yhandle = lhandle * np.cos(t)
    xpivot = lpivot * np.sin(t)
    ypivot = lpivot * np.cos(t) 

    # find piston location 
    dx = np.sqrt(lbar**2 - ypivot**2)
    xpiston = xpivot + dx
    return [xpivot, ypivot, xhandle, yhandle, xpiston]

def mechAdvantage(lhandle, lpivot, lbar, theta):
    # we are going to calculate and store three things
    # tt = the angle theta of the clamp. - zero is vertical
    # ll - the position of the plunger
    # dldr - the proportional change in the plunger compared to the change in the lever position
    #       - this is the leverage of the system and is associated with the clamping power
    tt = []
    ll = []

    # loop through the range of thetas
    for theta in range(0, 90):
        xpivot, ypivot, xhandle, yhandle, xpiston = calcPts(theta, lhandle, lpivot, lbar)
        tt.append(theta)
        ll.append(xpiston)

    # change in position per degree
    dr = lhandle * np.pi / 180.
    mechanical_advantage = []
    for theta in range(0, 89):
        dl = ll[theta+1] - ll[theta]
        mechanical_advantage.append(dr/dl)  

    print("  angle\t\tmechanical advantage")
    print("------------------------------")
    for theta in range(0,89, 5):
        print("{:5d}        {:7.2f} ".format(theta, mechanical_advantage[theta]))        

    # draw graphs with findings
    figure, axis = plt.subplots(1, 2, figsize=(13, 5))
    axis[0].set_title("position of the plunger vs theta")
    axis[0].set_xlabel("theta")
    axis[0].set_ylabel("position of the plunger")
    axis[0].text(0, 0, "test", fontsize=12)
    axis[0].plot(tt, ll, '-')

    axis[1].set_title("mechanical advantage vs theta")
    axis[1].set_xlabel("theta")
    axis[1].set_ylabel("mechanical advantage")
    axis[1].plot(tt[0:89], mechanical_advantage,'-')
    plt.show()


def computePoints():
    # compute points of toggle clamp
    xpivot, ypivot, xhandle, yhandle, xpiston = calcPts(28, 11, 10, 8.85)
    plt.xlim( -10, 120)
    plt.ylim( -10, 120)
    # plot the points
    plt.plot( [0,xpivot, xhandle], [0, ypivot, yhandle],"*-")
    plt.plot([xpivot, xpiston], [ypivot, 0],'*-')
    plt.show()


if __name__ == '__main__':
    mechAdvantage(20.32, 15, 13.43, 69)

