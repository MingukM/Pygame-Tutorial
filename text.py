#File Name: text.py
#Purpose: Inherit Drawable to display texts on screen as objects
#Name: Minguk Moon
#ID: mm5697
#Date: 2/22/24

import pygame
from drawable import Drawable

class Text(Drawable):

    def __init__(self, message = "Pygame", x=0, y=0, 
                 color = (0, 0, 0), size = 24):
        super().__init__(x, y)
        self.__message = message
        self.__color = color
        self.__fontObj = pygame.font.Font("freesansbold.ttf", size)

    # Implementation of abstract methods
    def draw(self, surface):
        self.__surface = self.__fontObj.render(self.__message, \
                                               True, self.__color)
        surface.blit(self.__surface, self.getLoc())

    def get_rect(self):
        return self.__surface.get_rect()
    
    # Accessors and mutators
    def setMessage(self, message):
        self.__message = message
    