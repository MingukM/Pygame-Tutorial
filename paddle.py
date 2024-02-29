#File Name: paddle.py
#Purpose: Inherit Drawble to create an paddle object
#         which moves with x position of the mouse
#Name: Minguk Moon
#ID: mm5697
#Date: 2/22/24

import pygame
from drawable import Drawable

class Paddle(Drawable):

    def __init__(self, width, height, color):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        super().__init__(screenWidth / 2, screenHeight / 2)

        self.__color = color
        self.__width = width
        self.__height = height

    # Implementation of abstract methods
    def draw(self, surface):
        pygame.draw.rect(surface, self.__color, self.get_rect())
    
    def get_rect(self):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()

        mouseX = pygame.mouse.get_pos()[0]
        
        return pygame.Rect(mouseX - self.__width / 2, \
                           screenHeight - 20 - (self.__height), \
                            self.__width, self.__height)
    
    # Mutator
    def setColor(self, color):
        self.__color = color
    
