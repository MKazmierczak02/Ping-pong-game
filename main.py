import sys
import pygame
from setting import *
pygame.init()

class Player:
    def __init__(self,side,paddle_color):
        self.width = 25
        self.height = 200
        self.side = side
        self.score = 0
        self.paddle_color = paddle_color
        if (side == 'left'):
            self.rect = pygame.Rect(0,(screen_height//2-self.height//2),self.width,self.height)
        else:
            self.rect = pygame.Rect((screen_width - self.width),(screen_height//2-self.height//2),self.width,self.height)
    
    def player_movement(self,pressed_keys):
        if self.side == 'left':
            if pressed_keys[pygame.K_w] and self.rect.y >5:
                self.rect.y-=VEL
            if pressed_keys[pygame.K_s] and self.rect.y + self.height < screen_height-5:
                self.rect.y+=VEL
        else:
            if pressed_keys[pygame.K_o] and self.rect.y >5:
                self.rect.y-=VEL
            if pressed_keys[pygame.K_k] and self.rect.y + self.height < screen_height-5:
                self.rect.y+=VEL
        

    def draw_player(self,pressed_keys):
        if self.side == 'left':
            self.score_text = LOGO_FONT.render(str(self.score),1,colors[self.paddle_color])
            SCREEN.blit(self.score_text,(self.score_text.get_width(),100))
        else:
            self.score_text = LOGO_FONT.render(str(self.score),1,colors[self.paddle_color])
            SCREEN.blit(self.score_text,(screen_width-self.score_text.get_width()*2,100))

        self.player_movement(pressed_keys)
        pygame.draw.rect(SCREEN,colors[self.paddle_color],self.rect)

class Ball:
    def __init__(self, ball_color):
        self.width = 30
        self.height = 30
        self.x_vel = 0 #7
        self.y_vel = 0
        self.y_maxvel = 10
        self.play_text = LOGO_FONT.render('Press SPACE to play!',1,'white')
        
        self.rect = pygame.Rect(screen_width//2-self.width//2,screen_height//2-self.height//2,self.width,self.height)
        self.up_border = pygame.Rect(0,0,screen_width,4)
        self.bot_border = pygame.Rect(0,screen_height-4,screen_width,4)
        self.ball_color = ball_color


    def ball_movement(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        
        
    def collisions(self,player_l,player_r):
            if self.rect.colliderect(player_l.rect):
                self.x_vel *= -1

                middle_y = player_l.rect.y + player_l.height//2
                difference_in_y = middle_y-(self.rect.y+self.height//2)
                reduction_factor = (player_l.height/2) / self.y_maxvel
                self.y_vel = difference_in_y/reduction_factor

            if self.rect.colliderect(player_r.rect):
                self.x_vel *=-1

                middle_y = player_r.rect.y + player_r.height//2
                difference_in_y = middle_y-(self.rect.y+self.height//2)
                reduction_factor = (player_r.height/2) / self.y_maxvel
                self.y_vel = difference_in_y/reduction_factor
            
            if self.rect.y +33 > self.bot_border.y:
                self.y_vel *= -1
            if self.rect.y<self.up_border.y:
                self.y_vel *= -1

            if self.rect.x < 0:
                player_r.score += 1
                self.y_vel = 0
                self.x_vel = 0
                self.rect.x = screen_width//2-self.width//2
                self.rect.y = screen_height//2-self.height//2
            if self.rect.x > screen_width:
                player_l.score += 1
                self.y_vel = 0
                self.x_vel =0
                self.rect.x = screen_width//2-self.width//2
                self.rect.y = screen_height//2-self.height//2                



    def draw_ball(self):
        self.ball_movement()
        if self.x_vel == 0:
            SCREEN.blit(self.play_text,(310,550))
        pygame.draw.rect(SCREEN,'red',self.up_border)
        pygame.draw.rect(SCREEN,'red',self.bot_border)
        pygame.draw.circle(SCREEN,colors[self.ball_color],(self.rect.x+15,self.rect.y+15),15)
        


def display(player_l,player_r, ball,pressed_keys,settings):
    SCREEN.fill(colors[settings.bg_color])
    ball.collisions(player_l,player_r)
    player_l.draw_player(pressed_keys)
    player_r.draw_player(pressed_keys)
    ball.draw_ball()
    pygame.display.update()



exit_text = LOGO_FONT.render('Return to main menu?',1,'white')
choices = ["Yes", "No"]


def display_exitask():
    ask = True
    position = 0
    while ask:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and position <1:
                    position+=1
                elif event.key == pygame.K_LEFT and position > 0:
                    position -= 1                

                if event.key == pygame.K_SPACE and position == 0:
                    return False
                if event.key == pygame.K_SPACE and position == 1:
                    ask = False
                    return True
               
    
        SCREEN.fill('black')
        SCREEN.blit(exit_text,(screen_width//2-exit_text.get_width()//2,250))
        for index, text in enumerate(choices):
                if index == position:
                    menu_text = MENU_FONT.render(text,1,'red')
                else:
                    menu_text = MENU_FONT.render(text,1,'white')
                SCREEN.blit(menu_text,((index+5.5)*100,400))



        pygame.display.update()
        CLOCK.tick(60)
            

    

        
        
def game(settings):
    player_l = Player('left',settings.paddle_color)
    player_r = Player('right',settings.paddle_color)
    ball1 = Ball(settings.ball_color)
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    play = display_exitask() 

                if event.key == pygame.K_SPACE:
                    if player_r.score>=player_l.score:
                        ball1.x_vel = -1*settings.vel
                    else :
                        ball1.x_vel = settings.vel
                    player_l.rect  = pygame.Rect(0,(screen_height//2-player_l.height//2),player_l.width,player_l.height)
                    player_r.rect = pygame.Rect((screen_width - player_r.width),(screen_height//2-player_r.height//2),player_r.width,player_r.height)
                if event.key == pygame.K_r:
                     player_l = Player('left',settings.paddle_color)
                     player_r = Player('right',settings.paddle_color)
                     ball1 = Ball()
        pressed_keys = pygame.key.get_pressed()
        display(player_l,player_r,ball1,pressed_keys,settings)
        CLOCK.tick(60)
        

