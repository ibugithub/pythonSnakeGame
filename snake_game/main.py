import pygame 
import time
from pygame.locals import *

def moveSnake():
    window.fill('#9966FF')
    window.blit(block, (posX, posY))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init() 
    window = pygame.display.set_mode((500, 500)) 
    window.fill('#9966FF')
    block = pygame.image.load('resources/block.jpg').convert()
    posX = 0
    posY = 0
    window.blit(block, (posX, posY))
    pygame.display.flip()

    should_stay = True
    
    while should_stay:
        for event in pygame.event.get():
            if event.type == KEYDOWN:

                if event.key == K_RIGHT: 
                    goRight = True
                    while goRight: 
                        posX += 10
                        time.sleep(.5)
                        moveSnake()
                if event.key == K_LEFT:
                    goRight = False
                    posX -= 10
                    moveSnake()
                if event.key == K_UP: 
                    posY -= 10
                    print(posY)
                    moveSnake()
                if event.key == K_DOWN:
                    posY += 10 
                    print(posY)
                    moveSnake()
            
            elif event.type ==   QUIT:
                should_stay = False