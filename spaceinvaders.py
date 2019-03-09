from __future__ import division
from pygame import *
from math import *
from random import *
from sys import *
from pygame.locals import *
import time

init()
screen = display.set_mode((1024,800))
width =1024
height = 800
display.set_caption("Space Invaders")
life_count=3

class Player:
    def __init__(self):
        self.sprite = image.load("Asteroids_Spaceship.png")
        self.upimage = self.sprite
        self.rect = self.sprite.get_rect()
        self.rect.centerx= width/2
        self.rect.centery= height-(height*(1/8))
        self.vx = 0
        self.vy = 0
        self.sprite = transform.rotate(self.upimage,90)

    def go_right(self):
        self.rect.centerx += 10

    def go_left(self):
      self.rect.centerx -= 10

    def blew_up(self):
        Player.remove(self)
        del(self)


    def update_and_display(self):
        self.rect.centerx += self.vx
        self.rect.centery += self.vy
        if Collide():
         import sys
         sys.exit()
        if self.rect.centerx < 0:
            self.rect.centerx = 1024
        if self.rect.centerx > 1024:
            self.rect.centerx = 0
        if self.rect.centery < 0:
            self.rect.centery = 800
        if self.rect.centery > 800:
            self.rect.centery = 0

        screen.blit(self.sprite, self.rect)
        
health_barr = 5  
class Barrier:
    def __init__(self, px, py):
        self.sprite = image.load("bar.png")
        self.rect = self.sprite.get_rect()
        self.px =px
        self.py =py
    def display(self):
        screen.blit(self.sprite, self.rect)
        if self.rect.centerx < 0:
            self.rect.centerx = 1024
        if self.rect.centerx > 1024:
            self.rect.centerx = 0
        if self.rect.centery < 0:
            self.rect.centery = 800
        if self.rect.centery > 800:
            self.rect.centery = 0
        self.rect.centerx = self.px
        self.rect.centery = self.py
barrier_xaxis=width/10
barrier_yaxis=height-(height*(2/8))
barriers=[Barrier(x,y) for x,y in [(barrier_xaxis,barrier_yaxis),(barrier_xaxis*4,barrier_yaxis),(barrier_xaxis*6,barrier_yaxis),(barrier_xaxis*8,barrier_yaxis),\
                                   (barrier_xaxis,barrier_yaxis+50),(barrier_xaxis*4,barrier_yaxis+50),(barrier_xaxis*6,barrier_yaxis+50),(barrier_xaxis*8,barrier_yaxis+50),\
                                   (barrier_xaxis+50,barrier_yaxis),((barrier_xaxis*4)+50,barrier_yaxis),((barrier_xaxis*6)+50,barrier_yaxis),((barrier_xaxis*8)+50,barrier_yaxis),\
                                   (barrier_xaxis+50,barrier_yaxis+50),((barrier_xaxis*4)+50,barrier_yaxis+50),((barrier_xaxis*6)+50,barrier_yaxis+50),((barrier_xaxis*8)+50,barrier_yaxis+50)]]
rand_kind=random() * 2

class Badmanners:
        def __init__(self, x, y):
            self.sprite = image.load("bull.png")
            self.rect = self.sprite.get_rect()
            self.rect.centery = y
            self.rect.centerx = x
            self.shell_vel =6
            self.shell_range= 800 
            self.d = 180
            self.m = 0
        def update_and_display(self):
            self.rect.centery += 20
            self.m += self.shell_vel
            screen.blit(self.sprite, self.rect)
            if self.m > self.shell_range:
                self.delete_self()

        def delete_self(self):
            enemy_shot.remove(self)
            del self
            
enemy_shot=[]

class alien:
    
    def __init__(self, px, py,rand_kind):
        if rand_kind <= 1:
             self.sprite = image.load("alien.png")
        if rand_kind > 1:
            self.sprite = image.load("alien2.png")
        self.rect = self.sprite.get_rect()
        self.px =px
        self.py =py
        self.direction = "right"
        
    def flight(self):
        if self.direction == "right":
            self.px -=4
        if self.direction == "left":
            self.px +=4
        
    def bang(self):
        aliens.remove(self)
        del(self)

    def display(self):
        alien.flight(a)
        screen.blit(self.sprite, self.rect)

        if self.rect.centerx < 0:
            self.rect.centerx = 1024
        if self.rect.centerx > 1024:
            self.rect.centerx = 0
        if self.rect.centery < 0:
            self.rect.centery = 800
        if self.rect.centery > 800:
            self.rect.centery = 0
        self.rect.centerx = self.px
        self.rect.centery = self.py

p = Player()
key.set_repeat(12,12)
alien_yaxis= height-(height*(7/8))
alien_xaxis=width/10
aliens = [alien(x, y,rand_kind) for x,y,rand_kind in [(alien_xaxis,alien_yaxis,rand_kind/10),(alien_xaxis*1.5,alien_yaxis-30,rand_kind*10),(alien_xaxis*.5,alien_yaxis-30,rand_kind*10),\
                                                      (alien_xaxis*2,alien_yaxis,rand_kind/10),(alien_xaxis*1.5,alien_yaxis,rand_kind/10),(alien_xaxis*2.5,alien_yaxis-30,rand_kind*10),\
                                                      (alien_xaxis*3,alien_yaxis,rand_kind/10),(alien_xaxis*2.5,alien_yaxis,rand_kind/10),(alien_xaxis*3.5,alien_yaxis-30,rand_kind*10),\
                                                      (alien_xaxis*4,alien_yaxis,rand_kind/10),(alien_xaxis*3.5,alien_yaxis,rand_kind/10),(alien_xaxis*4.5,alien_yaxis-30,rand_kind*10),\
                                                      (alien_xaxis*5,alien_yaxis,rand_kind/10),(alien_xaxis*4.5,alien_yaxis,rand_kind/10),(alien_xaxis*5.5,alien_yaxis-30,rand_kind*10),\
                                                      (alien_xaxis*6,alien_yaxis,rand_kind/10),(alien_xaxis*5.5,alien_yaxis,rand_kind/10),(alien_xaxis*6.5,alien_yaxis-30,rand_kind*10),\
                                                      (alien_xaxis*7,alien_yaxis,rand_kind/10),(alien_xaxis*6.5,alien_yaxis,rand_kind/10),(alien_xaxis*7.5,alien_yaxis-30,rand_kind*10),\
                                                      (alien_xaxis*8,alien_yaxis,rand_kind/10),(alien_xaxis*7.5,alien_yaxis,rand_kind/10),(alien_xaxis*8.5,alien_yaxis-30,rand_kind*10),\
                                                      (alien_xaxis*9,alien_yaxis,rand_kind/10),(alien_xaxis*8.5,alien_yaxis,rand_kind/10),(alien_xaxis*.5,alien_yaxis,rand_kind/10),\
                                                      (alien_xaxis*1,alien_yaxis-30,rand_kind*10),(alien_xaxis*2,alien_yaxis-30,rand_kind*10),(alien_xaxis*3,alien_yaxis-30,rand_kind*10),\
                                                      (alien_xaxis*4,alien_yaxis-30,rand_kind*10),(alien_xaxis*5,alien_yaxis-30,rand_kind*10),(alien_xaxis*6,alien_yaxis-30,rand_kind*10),\
                                                      (alien_xaxis*7,alien_yaxis-30,rand_kind*10),(alien_xaxis*8,alien_yaxis-30,rand_kind*10),(alien_xaxis*9,alien_yaxis-30,rand_kind*10),\
                                                      (alien_xaxis*9.5,alien_yaxis,rand_kind/10),(alien_xaxis*9.5,alien_yaxis-30,rand_kind*10)]]

def Collide():
    collide_r = p.sprite.get_rect()
    collide_r.w = 80
    collide_r.h = 80
    collide_r.centerx = p.rect.centerx
    collide_r.centery = p.rect.centery
    for a in aliens:
        if a.rect.colliderect(collide_r):
            return True
    return False

def Shell_hit():
    for a in aliens:
        for s in shells:
            if a.rect.colliderect(s.rect):
                aliens.remove(a)
                del a
                shells.remove(s)
                del s
                Shell_hit()
                return

def Death_count():
    global life_count
    for e in enemy_shot:
        if p.rect.colliderect(e.rect):
            if life_count == 1:
                print("GAME OVER!!!")
                sys_font=font.SysFont("None",60)
                rendered= sys_font.render('Game Over', 0 , (80,200,80))
                screen.blit(rendered,(500,400))
                quit()
                exit()
                
            else:
                life_count -=1
                enemy_shot.remove(e)

def Barr_hit():
    for b in barriers:
        for e in enemy_shot:
            if b.rect.colliderect(e.rect):
                enemy_shot.remove(e)
                barriers.remove(b)
def friendly_fire():
    for b in barriers:
        for s in shells:
            if b.rect.colliderect(s.rect):
                shells.remove(s)
                barriers.remove(b)
        
score=0                
def Score():
    global score
    if len(aliens):
        score= ((36- (len(aliens))+2)*100 )
    if len(aliens)== 0:
        score=3800
    total ='score ' + str(score)
    sys_font=font.SysFont("None",60)
    rendered= sys_font.render(total, 0 , (80,200,80))
    screen.blit(rendered,(800,750))
    
def Win():
    if len(aliens)==0:
        sys_font=font.SysFont("None",60)
        rendered= sys_font.render('You Win', 0 , (80,200,80))
        screen.blit(rendered,(500,400))
def Lives_left():
    global life_count
    sys_font=font.SysFont("None",60)
    rendered= sys_font.render('lives ' + str(life_count), 0 , (80,200,80))
    screen.blit(rendered,(75,750))
    
shell_vel =6
shell_range= 800

class Shell:
    def __init__(self, x, y):
        self.d = 90
        self.sprite = image.load("bull.png")
        self.rect = self.sprite.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.m = 0

    def update_and_display(self):
        self.rect.centery -= 20
        self.m += shell_vel
        screen.blit(self.sprite, self.rect)
        if self.m > shell_range:
            self.delete_self()

    def delete_self(self):
        shells.remove(self)
        del self

    def kaboom(self):
        shells.remove(self)
        del(self)

shells = []


while True:
    
    for e in event.get():  
        if e.type == KEYDOWN:
            if e.key == K_RIGHT or e.key == K_d:
               p.go_right()
            if e.key == K_LEFT or e.key == K_a:
                p.go_left()
            if e.key == K_SPACE:
                shells.append(Shell(p.rect.centerx, p.rect.centery))
        
        if e.type == QUIT:
            quit()
            exit()
    
    for a in aliens:
        if (randint(0,750) == 0):
            enemy_shot.append(Badmanners(a.rect.centerx,a.rect.centery))
        if a.px <= 0:
            a.direction = "left"
            a.py +=60
            if a.py > 800:
                a.delete_self
        if a.px  >= 1024:
            a.direction = "right"
            a.py +=60
            if a.py > 800:
                a.delete_self

   
    screen.fill((0, 0, 0))
    Shell_hit()
    Score()
    Win()
    Barr_hit()
    Lives_left()
    Death_count()
    friendly_fire()
    for b in barriers:
        b.display()
    p.update_and_display()
    for s in shells:
        s.update_and_display()
    time.sleep(.03)
    for a in aliens:
       a.display()
    for e in enemy_shot:
        e.update_and_display()
    display.flip()
