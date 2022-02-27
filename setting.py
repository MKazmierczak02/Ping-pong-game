import pygame
import sys

pygame.font.init()
screen_width = 1290
screen_height = 720

SCREEN = pygame.display.set_mode((screen_width, screen_height))
CLOCK = pygame.time.Clock()

VEL = 4
paddle_color = 0
ball_color = 1
bg_color = 2

colors = ['grey','white','black','red','green','blue','yellow','cyan','pink']
choices = ['paddle color', 'ball color', 'bg color', 'ball speed']

LOGO_FONT = pygame.font.SysFont("comicsans", 100)
MENU_FONT = pygame.font.SysFont("comicsans", 65)
SCORE_FONT = pygame.font.SysFont("comicsans", 30)
SETTING_FONT =pygame.font.SysFont("comicsans",45)

settings_text = LOGO_FONT.render('Settings',1,'white')
color_text = SCORE_FONT.render(colors[paddle_color],1,'white')

class Settings:
    def __init__(self,paddle_color,ball_color,bg_color,VEL):
        self.paddle_color = paddle_color
        self.ball_color = ball_color
        self.bg_color = bg_color
        self.vel = VEL
    
    

def settings_fun(settings):
    ask = True
    position = 0
    global paddle_color
    global ball_color
    while ask:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ask = False
                if event.key == pygame.K_RIGHT and position <3:
                    position+=1
                elif event.key == pygame.K_LEFT and position > 0:
                    position -= 1
                if event.key==pygame.K_UP and position == 0 and settings.paddle_color < len(colors)-1:      
                    settings.paddle_color +=1
                if event.key==pygame.K_DOWN and position == 0 and settings.paddle_color > 0:
                    settings.paddle_color -=1
                if event.key==pygame.K_UP and position == 1 and settings.ball_color < len(colors)-1:      
                    settings.ball_color +=1
                if event.key==pygame.K_DOWN and position == 1 and settings.ball_color > 0:
                    settings.ball_color -=1
                if event.key==pygame.K_UP and position == 2 and settings.bg_color < len(colors)-1:      
                    settings.bg_color +=1
                if event.key==pygame.K_DOWN and position == 2 and settings.bg_color > 0:
                    settings.bg_color -=1
                if event.key==pygame.K_UP and position == 3 and settings.vel < 20:     
                    settings.vel +=1
                if event.key==pygame.K_DOWN and position == 3 and settings.vel > 0:
                    settings.vel -=1
                



        paddle_color_text = SETTING_FONT.render(colors[settings.paddle_color],1,'white')
        ball_color_text = SETTING_FONT.render(colors[settings.ball_color],1,'white')
        bg_color_text = SETTING_FONT.render(colors[settings.bg_color],1,'white')
        vel_text = SETTING_FONT.render(str(settings.vel),1,'white')

        
        values = [paddle_color_text,ball_color_text,bg_color_text,vel_text]

        SCREEN.fill('black')
        SCREEN.blit(settings_text,(screen_width//2-settings_text.get_width()//2,100))

        for index,setting in enumerate(choices):
            if index == position:
                setting_text = MENU_FONT.render(setting,1,'red')
            else:
                setting_text = MENU_FONT.render(setting,1,'white')
            SCREEN.blit(setting_text,((index+1)*(screen_width//4)-setting_text.get_width()-30,300))
            SCREEN.blit(values[index],((index+1)*(screen_width//4)-setting_text.get_width()//2-30-values[index].get_width()//2,500))

        
        pygame.display.update()
        CLOCK.tick(60)