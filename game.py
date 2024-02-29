#File Name: game.py
#Purpose: Run the game with objects created by imported classes
#Name: Minguk Moon
#ID: mm5697
#Date: 2/22/24

import pygame
import random
from ball import Ball
from paddle import Paddle
from text import Text

# Initializing the game
pygame.init()
surface =  pygame.display.set_mode((800, 600))

# Colors
DREXEL_BLUE = (7, 41, 77) 
VEGAS_GOLD = (196, 180, 84)
SALMON = (250, 128, 114)
DEEPPINK = (255, 20, 147)
CORAL = (255, 99, 71)
PLUM = (221, 160, 221)
MEDIUMORCHID = (186, 85, 211)
LIME = (0, 255, 0)
MEDIUMAQUAMARINE = (102, 205, 170)
SANDYBROWN = (244, 164, 96)
GHOSTWHITE = (248, 248, 255)

colors = [DREXEL_BLUE, \
          VEGAS_GOLD, \
          SALMON, \
          DEEPPINK, \
          CORAL, \
          PLUM, \
          MEDIUMORCHID, \
          LIME, \
          MEDIUMAQUAMARINE,\
          SANDYBROWN, \
          GHOSTWHITE]

# Counters
numHits = 0
myHealth = 3

# Value to allow toggling active objs and
# display update with space bar
pause = False

# Randomize initial position of the ball
posX = random.randint(50, 750)
posY = random.randint(50, 200)

# Drawble objects
myBall = Ball(posX, posY, 25, DREXEL_BLUE)
myPaddle = Paddle(200, 25, VEGAS_GOLD)
myScoreBoard = Text("Score: 0", 10, 10)
myLife = Text("Life: 3", 370, 10)
youWin = Text("You Win!", 310, 290, size = 40)
gameOver = Text("Game Over!", 290, 290, size = 40)

# Custom events
WIN = pygame.USEREVENT + 1
LOST = pygame.USEREVENT + 2

# Game loop to update the display
fpsClock = pygame.time.Clock()
running = True
while running:
    surface.fill((255, 255, 255))

    # Testing get_rect method 
    # pygame.draw.rect(surface, (123, 123, 123), myBall.get_rect())

    # Drawing drawble objects on screen
    myBall.draw(surface)
    myPaddle.draw(surface)
    myScoreBoard.draw(surface)
    myLife.draw(surface)

    # Allow ball to bounce off the paddle
    # Ball accelerates each time it bounces off the paddle
    # also both objects change each of their colors
    if myBall.intersects(myPaddle):

        if myBall.getYSp() < 0:
            myBall.setYSp((myBall.getYSp() - 1)*-1)
        else:
            myBall.setYSp((myBall.getYSp() + 1)*-1)

        if myBall.getXSp() < 0:
            myBall.setXSp(myBall.getXSp() - 1)
        else:
            myBall.setXSp(myBall.getXSp() + 1)

        myBall.setColor(colors[random.randint(0, len(colors) - 1)])
        myPaddle.setColor(colors[random.randint(0, len(colors) - 1)])

        numHits += (1 * myBall.scoreMultiplier())
        myScoreBoard.setMessage("Score: " + str(numHits))

    # Deduct one life if the player fails to stop the ball
    # from going out of screen through bottom of the screen
    if myBall.outOfScreen():
        myHealth -= 1
        myLife.setMessage("Life: " + str(myHealth))

        if numHits > 10:
            numHits -= 2 * (numHits // 10)
        myScoreBoard.setMessage("Score: " + str(numHits))
        
        if myBall.getXSp() > 15:
            myBall.setXSp(int(myBall.getXSp() * 2/3))
        if myBall.getYSp() > 15:
            myBall.setYSp(int(myBall.getYSp() * 2/3))

        posX = random.randint(50, 750)
        posY = random.randint(50, 150)
        myBall.setLoc((posX, posY))

    # Winning condition
    # Displays You Win! on the screen
    # through event handling
    if numHits >= 50:
        pygame.event.post(pygame.event.Event(WIN))

    # Losing condition
    # Displays Game Over! on the screen
    # through event handling
    if myHealth <= 0:
        pygame.event.post(pygame.event.Event(LOST))

    # Animate the ball
    if numHits <= 50 and myHealth > 0 and not pause:    
        myBall.move_ball()

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False
        # Testing visible
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     myBall.setVisible(not myBall.isVisible())
        
        # Handling toggling the animation
        elif event.type == pygame.KEYDOWN:
            if event.__dict__['key'] == pygame.K_SPACE:
                if pause:
                    pause = False
                else:
                    pause = True

        # Handling the event for winning
        elif event.type == WIN:
            surface.fill((255, 255, 255))
            youWin.draw(surface)
            pygame.display.update()
            pause = True
            
        # Handling the event for losing
        elif event.type == LOST:
            surface.fill((255, 255, 255))
            gameOver.draw(surface)
            pygame.display.update()
            pause = True
    
    if not pause:   
        pygame.display.update()
        fpsClock.tick(30)
exit()