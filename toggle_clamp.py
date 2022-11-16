# Design analysis for a linear toggle clamp 
# Inspired by https://www.instructables.com/The-Linear-Toggle-Clamp/
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from matplotlib import rc


def calcPts(theta, lhandle, lpivot, lbar):
    t = (theta * np.pi) / 180
    xhandle = lhandle * np.sin(t)
    yhandle = lhandle * np.cos(t)
    xpivot = lpivot * np.sin(t)
    ypivot = lpivot * np.cos(t) 

    # find piston location 
    dx = np.sqrt(lbar**2 - ypivot**2)
    xpiston = xpivot + dx

    #return [abs(xpivot), abs(ypivot), abs(xhandle), abs(yhandle), abs(xpiston)]
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
    for theta in range(0,89, 1):
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


def animateFunc(frame_number):  
    # clamp constants
    angle = 90
    theta_min = 30
    theta_max = 96.74
    lhandle = 20
    lpivot = 15
    lbar = 13
    lplunger = 12
    xbase_min = -13
    xbase_max = 60

    dtheta =  float(theta_max - theta_min) / float(49)
    theta = (frame_number * dtheta) + theta_min  
    # ugly hack below to get the 'correct' physics of the clamp
    # using a stack to 'step-back' to the previous thetas
    if (frame_number < (max_frames/2)):
        prev_thetas.append(theta)
    else:
        theta = prev_thetas.pop()

    # calculate points along the clamp
    xpivot, ypivot, xhandle, yhandle, xpiston = calcPts(theta, lhandle, lpivot, lbar)

    # set up the animation
    ax.clear()
    plt.title("Linear Clamp System Animation")
    ax.set_xlim(-80,180)
    ax.set_ylim(-20,110)
    ax.set_aspect(1)

    if print_points:
        print('frame number: ' + str(frame_number))
        print('theta: ' + str(theta))
        print('xpivot: ' + str(xpivot))
        print('xhandle: ' + str(xhandle))
        print('xpiston: ' + str(xhandle))
        print('ypivot: ' + str(ypivot))
        print('yhandle: ' + str(yhandle))
        print('xpiston-lplunger/2: ' + str(xpiston-lplunger/2))
        print('xpiston+lplunger/2: ' + str(xpiston+lplunger/2))
        print('\n')

    ax.plot([0, xpivot, xhandle], [0, ypivot, yhandle], "*-", linewidth=3, label="lever")
    ax.plot([xpivot, xpiston], [ypivot, 0], '*-',linewidth=3, label="arm")
    ax.plot([xpiston-lplunger/2, xpiston+lplunger/2],[0,0], linewidth=3, label="plunger")
    ax.plot([xbase_min, xbase_max], [-5,-5], linewidth=3, label="base")

    ax.legend()
    ax.plot()

    if (frame_number == (max_frames/2)):
        plt.savefig('clamp_locked.png')



def computePoints():
    # compute points of toggle clamp
    xpivot, ypivot, xhandle, yhandle, xpiston = calcPts(28, 11, 10, 8.85)
    plt.xlim( -10, 120)
    plt.ylim( -10, 120)
    # plot the points
    plt.plot( [0,xpivot, xhandle], [0, ypivot, yhandle],"*-")
    plt.plot([xpivot, xpiston], [ypivot, 0],'*-')
    plt.show()


def makeAnimation():
    # nasty hacky globals!
    global fig
    global ax
    global print_points
    global max_frames
    global prev_thetas 

    prev_thetas = []    
    print_points = True
    max_frames = 100
    fig = plt.figure(figsize=(8,6))
    ax = plt.axes()
    anim = animation.FuncAnimation(fig, animateFunc, frames=max_frames+1, blit=False, repeat=True, interval=10)
    anim_video = animation.PillowWriter(fps=60)
    anim.save('system.gif', writer=anim_video)
    plt.show()


def testSingleFrame():
    handle_open_theta = (29.90 * np.pi) / 180 # handle angle at open position
    link_open_theta = (118.57 * np.pi) / 180  # handle link at open position
    angle = 65
    theta_min = 27
    theta_max = angle
    frameMax = 50
    dtheta =  float(theta_max - theta_min) / float(frameMax-1)
    theta = 0 * dtheta - angle

    lhandle = 20
    lpivot = 15
    lbar = 13
    lplunger = 12
    xbase_min = -13
    xbase_max = 60

    # calculate the key pionts
    xpivot, ypivot, xhandle, yhandle, xpiston = calcPts(theta, lhandle, lpivot, lbar)

    # set up the graph
    plt.title("diagram of the clamp")
    plt.xlim(-80,180)
    plt.ylim(-20,110)
    #plt.aspect(1)

    print('theta: ' + str(theta))
    print('dtheta: ' + str(dtheta))
    print('xpivot: ' + str(xpivot))
    print('xhandle: ' + str(xhandle))
    print('xpiston: ' + str(xhandle))
    print('ypivot: ' + str(ypivot))
    print('yhandle: ' + str(yhandle))
    print('xpiston-lplunger/2: ' + str(xpiston-lplunger/2))
    print('xpiston+lplunger/2: ' + str(xpiston+lplunger/2))
    print('\n')

    # find initial positions of the handle
    y_handle = 2 * np.cos(handle_open_theta)
    y_pivot =  10 * np.cos(handle_open_theta)

    # find inital position of arm link 
    y_arm_link_handle = None
    y_arm_link_plunger = 15 * np.cos(link_open_theta)

    # plot the points
    plt.plot( [0, 2, 10], [0, y_handle, y_pivot], "*-", linewidth=3, label="lever")
    plt.plot([10, 15], [y_pivot, link_open_theta], '*-',linewidth=3, label="arm")
    plt.plot([15, 30],[link_open_theta, link_open_theta], linewidth=3, label="plunger")
    plt.plot([xbase_min, xbase_max], [-5,-5], linewidth=3, label="base")
    
    plt.show()


if __name__ == '__main__':
    #mechAdvantage(22.15, 15, 13.75, 32.7)
    #testSingleFrame()
    makeAnimation()