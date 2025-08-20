from pygame import *
from time import time as timer

font.init()
font2 = font.Font(None,36)

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,weight,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(weight,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

    

class Player(GameSprite):
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_weight - 80:
            self.rect.y += self.speed
        
        if self.rect.centery < ball.rect.centery - 5 and ball.rect.centerx < win_weight / 2:
            self.rect.y += self.speed
        if self.rect.centery > ball.rect.centery + 5 and ball.rect.centerx < win_weight / 2:
            self.rect.y -= self.speed

        if self.rect.y < 5:
            self.rect.y = 5
        if self.rect.y > win_weight - 150:
            self.rect.y = win_height - 150
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        


    


back = (200,255,255)
speed_x = 3
speed_y = 3
win_weight = 600
win_height = 500
window = display.set_mode((win_weight,win_height))
back = transform.scale(image.load('background.png'),(win_weight,win_height))


game = True
finish = False
clock = time.Clock()
fps = 60

racket1 = Player('racket.png',30,200,4,50,150)
racket2 = Player('racket.png',520,200,4,50,150)
ball = GameSprite('asteroid.png',200,200,4,50,50)

lose1 = font2.render('Player 1 lose',1,(180,0,0))
lose2 = font2.render('Player 2 lose',1,(180,0,0))






difficulty_add = False


show_text1 = True

#Цикл
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False

    if finish != True:
        window.blit(back,(0,0))
        racket1.update_r()
        racket2.update_l()

        lives1 = font2.render('Жизни: 3',1,(0, 128, 0))
        window.blit(lives1,(20,20))
        lives2 = font2.render('Жизни: 3',1,(0, 128, 0))
        window.blit(lives2,(450,20))
        

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
        
        if ball.rect.bottom > win_height or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < -50:
            
            
            finish = True
            window.blit(lose1,(200,200))

        if ball.rect.x > win_weight:
            lives_2_2 = font2.render('Жизни: 2',1,(255, 165, 0))
            window.blit(lives_2_2,(450,20))
            
            ball.reset()
            
            window.blit(lose2,(200,200))

        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()
    clock.tick(fps)
