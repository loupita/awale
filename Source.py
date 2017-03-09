'''
Created on 8 mars 2017

@author: Utilisateur
'''
import sys

import pygame

from Jeu import Jeu




class Mouse():
    def __init__(self):
        self.on=False
        
    def check(self):
        if self.on==False and pygame.mouse.get_pressed()[0]==1:
            self.on=True
            return False
    
        if self.on==True and pygame.mouse.get_pressed()[0]==0:
            self.on=False
            return True
        
        return False
            

if __name__ == '__main__':
      
          
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    done = False
    c = pygame.time.Clock()
    bgg=pygame.image.load("img/wood.jpg")
    awa=pygame.image.load("img/awa.png")
    
    
    jeu=Jeu("Hollande"," Obama",contreIa=True)
    
    myfont = pygame.font.SysFont("monospace", 50)

    mouse=Mouse()
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
        
   
        screen.blit(bgg,(0,0))
        screen.blit(awa,(150,150))
        jeu.printG(myfont, screen)
        
        if mouse.check():
            jeu.mouseChech(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        pygame.display.flip()
        
