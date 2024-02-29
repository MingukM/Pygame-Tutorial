#File Name: ball.py
#Purpose: Inherit Drawable to create a ball object to play with
#Name: Minguk Moon
#ID: mm5697
#Date: 2/22/24

import random
import pygame
from drawable import Drawable

class Ball(Drawable):

    def __init__(self, x=0, y=0, radius = 10, color = (0, 0, 0)):
        super().__init__(x, y)
        self.__XSp = 8
        self.__YSp = 8
        self.__radius = radius
        self.__color = color
    
    # Implementation of abstract methods
    # Draw the ball
    def draw(self, surface):
        if self.isVisible():
            pygame.draw.circle(surface, self.__color, \
                               self.getLoc(), self.__radius)
    
    # Get the hit box of the ball
    def get_rect(self):
        location = self.getLoc()
        radius = self.__radius
        return pygame.Rect(location[0] - radius, location[1] - radius, \
                              2 * radius, 2 * radius)
    
    # Accessors and mutators
    def getColor(self):
        return self.__color
    def setColor(self, color):
        self.__color = color

    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius = radius
    
    def getXSp(self):
        return self.__XSp
    def setXSp(self, XSp):
        # Limiting the speed to 100
        if self.__XSp <= 98:
            self.__XSp = XSp

    def getYSp(self):
        return self.__YSp
    def setYSp(self, YSp):
        # Limiting the speed to 100
        if self.__YSp <= 98:
            self.__YSp = YSp


    # Method to allow a Ball object to move around on the screen
    def move_ball(self):
        x, y = self.getLoc()

        newX = x + self.__XSp
        newY = y + self.__YSp

        self.setX(newX)
        self.setY(newY)

        # Allows ball to bounce off sides of screen
        # except the bottom side of the screen
        surface = pygame.display.get_surface()
        width, height = surface.get_size()

        if newX <= self.__radius or newX + self.__radius >= width:
            self.__XSp *= -1
        if newY <= self.__radius:
            self.__YSp *= -1
    
    # Detects if the ball went out of screen below
    def outOfScreen(self):
        surface = pygame.display.get_surface()
        width, height = surface.get_size()

        if self.getY() - self.__radius >= height:
            return True
        else:
            return False
    
    # Score multiplier as the ball accelerates
    def scoreMultiplier(self):
        if self.__XSp < 0:
            XSp = self.__XSp * -1
            if XSp // 10 > 0:
                return XSp // 10
            else:
                return 1
        elif self.__XSp >= 0:
            if self.__XSp // 10 > 0:
                return self.__XSp // 10
            else:
                return 1
        else:
            return 1

