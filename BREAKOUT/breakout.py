"""
Created on Thu Feb  8 01:26:56 2018

@author: warrenl0134
"""

from graphics import *
from random import *

# height and width of game's window in pixels
HEIGHT = 600
WIDTH = 400

# number of rows and columns of bricks
ROWS = 5
COLS = 10

# radius of ball in pixels
RADIUS = 10

# size of paddle in pixels
PADWIDTH = 60
PADHT = 10

# number of lives
LIVES = 3

# brick size
BRKWDTH = (WIDTH - COLS) / COLS - 4
BRKHT = 10

# bricks list (array)
bricks = []

# instantiate window
win = GraphWin("Breakout", WIDTH, HEIGHT)


def main():
   # instantiate bricks
   initBricks()

   # instantiate ball, centered in middle of window
   ball = initBall()

   # instantiate paddle, centered at bottom of window
   paddle = initPaddle()

   # instantiate scoreboard, centered in middle of window
   label = initScoreboard()

   # number of lives initially
   lives = LIVES

   # instantiate lives scorekeeper
   livesText = initLives()

   # number of points initially
   score = 0

   # number of bricks initially
   numBricks = COLS * ROWS

   # initial velocity
   xvelocity = (random() * 0.03 + 0.02)
   yvelocity = 0.03

   # wait for mouse click
   win.getMouse()

   # play game
   while True:

       # move ball move using xvelocity, yvelocity
       ball.move(xvelocity, yvelocity)

       # get x and y coordinate of center of ball (xBall, yBall)
       centerBall = ball.getCenter()
       xBall = centerBall.getX()
       yBall = centerBall.getY()

       # bounce off edge of window
       if xBall + 20 > 400:
           xvelocity = -xvelocity
       elif xBall - 20 < 0:
           xvelocity = -xvelocity

       # if ball goes below paddle, decrease lives by 1
       # if no more lives, game over, else sleep 2 seconds and
       # instantiate new ball
       if yBall - 20 > 495:
           lives = lives - 1
           updateLives(livesText, lives)
           ball.undraw()
           if lives == 0:
               gameOver(label)
           else:
               time.sleep(2)
               ball = initBall()

       # paddle movement
       paddleMove(paddle)

       # if paddle hits ball reverse ball direction
       if padHit(paddle, xBall, yBall):
           yvelocity = -yvelocity

       # detect collision with bricks
       for brick in bricks:
           # if ball collides with a brick, undraw the brick
           # remove the brick from the list (bricks.remove(brick))
           # reverse the yvelocity
           # decrease the number of bricks by 1
           # increase the score by 1
           # update the scoreboard
           # if no more brickes left you win!
           if checkCollision(brick, yBall, xBall):
               brick.undraw()
               bricks.remove(brick)
               yvelocity = -yvelocity
               score = score + 1
               updateScoreboard(label, score)

   # wait for click before exiting
   win.getMouse()
   win.close()

   # all done!
   exit(0)


def initBricks():
   color = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE"]

   for i in range(ROWS):
       for j in range(COLS):
           x = j * (BRKWDTH + 5) + 2
           y = i * (BRKHT + 5) + 2
           rect = Rectangle(Point(x, y), Point(x + BRKWDTH, y + BRKHT))
           rect.setFill(color[i])
           rect.draw(win)
           bricks.append(rect)


# instantiate paddle as a rectangle object, in bottom middle of window
def initPaddle():
   paddle = Rectangle(Point(200 - PADWIDTH / 2, 500 - PADHT / 2), Point(200 + PADWIDTH / 2, 500 + PADHT / 2))
   paddle.setFill("black")
   paddle.draw(win)
   return paddle


# instantiate ball as a circle in center of window below the scoreboard
def initBall():
   center = Point(200, 300)
   ball = Circle(center, RADIUS)
   ball.setFill("black")
   ball.draw(win)
   return ball


# if ball touches left or right side of window, return True, else return False
def checkSides(xBall):
   xBall = ball.getX()
   while xBall == 0 or xBall == 400:
       return True
   return False


def paddleMove(paddle):
   user_event = win.checkKey()
   padPt = paddle.getP1()
   padX = padPt.getX()
   if user_event == "Left" and padX > 0:
       paddle.move(-20, 0)
   elif user_event == "Right" and padX + PADWIDTH < WIDTH:
       paddle.move(20, 0)


def padHit(paddle, xBall, yBall):
   pointPaddle = paddle.getP1()
   xPaddle = pointPaddle.getX()
   yPaddle = pointPaddle.getY()
   if xBall + RADIUS >= xPaddle and xBall - RADIUS <= (
       xPaddle + PADWIDTH) and yPaddle - yBall < 10 and yPaddle - yBall > -10:
       return True
   else:
       return False


def initLives():
   anchorpoint = Point(60, HEIGHT - 20)
   livesText = Text(anchorpoint, "Lives Remaining: " + str(LIVES))
   livesText.draw(win)
   return livesText


def updateLives(livesText, lives):
   livesText.setText("Lives Remaining: " + str(lives))
   return livesText


def initScoreboard():
   x = WIDTH / 2
   y = HEIGHT / 2
   anchorPoint = Point(x, y)
   label = Text(anchorPoint, "0")
   label.setSize(36)
   label.setTextColor("Dark Gray")
   label.draw(win)
   return label


def checkCollision(brick, yBall, xBall):
   brickCorner = brick.getP2()
   xBrick = brickCorner.getX()
   yBrick = brickCorner.getY()
   if yBall - yBrick < 5 and xBall > (xBrick - BRKWDTH) and xBall < xBrick:
       return True
   else:
       return False


def updateScoreboard(label, score):
   label.setText(score)
   return label


def gameOver(label):
   updateScoreboard(label, "You Lose!")
   time.sleep(4)
   exit(0)


def youWin(label):
   updateScoreboard(label, "You Win!")
   time.sleep(4)
   exit(0)


if __name__ == "__main__":
   main()

