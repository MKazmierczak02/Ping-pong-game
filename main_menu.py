import sys
import pygame

from setting import *
from main import *

pygame.init()


logo_text = LOGO_FONT.render('Ping Pong',1,'white')
menu = ["Play", "Settings", "Exit"]


def display(position):
    SCREEN.fill("black")
    SCREEN.blit(logo_text,(screen_width//2-logo_text.get_width()//2,100))
    for index, text in enumerate(menu):
        if index == position:
            menu_text = MENU_FONT.render(text,1,'red')
        else:
            menu_text = MENU_FONT.render(text,1,'white')
        SCREEN.blit(menu_text,(screen_width//2-menu_text.get_width()//2,(index+3)*100))
    pygame.display.update()
    
settings = Settings(paddle_color,ball_color,bg_color,VEL)
def menu_func():       
    position =0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and position <2:
                    position+=1
                elif event.key == pygame.K_UP and position > 0:
                    position -= 1
                if event.key == pygame.K_SPACE and position == 0:
                    game(settings)
                if event.key == pygame.K_SPACE and position == 1:
                    settings_fun(settings)
                
                if event.key == pygame.K_SPACE and position == 2:
                    pygame.quit
                    sys.exit()

        
        display(position)

        CLOCK.tick(60)
        
menu_func()
