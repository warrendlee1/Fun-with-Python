from graphics import *

# instantiate window
win = GraphWin("window", 320, 240)
win.setBackground('turquoise')
# instantiate a point with (x, y) coordinates of (160, 120)
center = Point(160, 120)

# instantiate ball with center at (160, 120)
ball = Circle(center, 20)

# fill the circle with black
ball.setFill("blue")

# draw the circle to the window
ball.draw(win)

velocity = .06
    
while True:

    # move ball along x-axis or y-axis
    ball.move(velocity, velocity)

    # get x-coordinate of circle
    centerBall = ball.getCenter()
    xBall = centerBall.getX()

    # bounce off right edge of window
    if xBall + 20 > 320:
        velocity = -velocity

    # bounce off left edge of window
    elif xBall - 20 < 0:
        velocity = -velocity

    # if there is a mouse click on window, close the window
    if win.checkMouse():
        win.close()
        break

exit(0)
