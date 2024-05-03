import pygame 
import datetime
pygame.init()
w,h=829,836
screen=pygame.display.set_mode((w,h))
fps=24
background=pygame.image.load("images\main-clock.png")
clock=pygame.time.Clock()

minhand=pygame.image.load("images\hand1.png")
sechand=pygame.image.load("images\left-hand.png")

min_rect=minhand.get_rect()
min_rect.center=((400,400))

secret=sechand.get_rect()
secret.center((400,400))

#make a time for this clock

current_time=datetime.datetime.now()

secvalue1=current_time.second
min_value=current_time.minute


run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
            exit()
    screen.blit(background,(0,0))
    genminhand=pygame.transform.rotate(minhand,-1*((6*min_value)%360))
    genminrect=genminhand.get_rect()
    genminrect.center=min_rect.center

    screen.blit(genminhand,genminrect)
    
