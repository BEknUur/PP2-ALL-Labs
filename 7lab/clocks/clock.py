import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((829,836))
pygame.display.set_caption("Clock for no reason")
icon = pygame.image.load("images\main-clock.png")
pygame.display.set_icon(icon)
fps = 24
background = pygame.image.load("images\main-clock.png")

clock = pygame.time.Clock()

minhand = pygame.image.load("images\hand1.png")
sechand = pygame.image.load("images\left-hand.png")

minrect = minhand.get_rect()
minrect.center = ((400,400))

secrect =sechand.get_rect()
secrect.center = (400,400)

currenttime = datetime.datetime.now()
secvalue1 = currenttime.second
minvalue1 = currenttime.minute

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()

    screen.blit(background, (0,0))
    genminhand = pygame.transform.rotate(minhand, -1*((6*minvalue1)%360))
    genminrect = genminhand.get_rect()
    genminrect.center = minrect.center
 
    screen.blit(genminhand,genminrect)

    gensechand = pygame.transform.rotate(sechand, -1*((6*secvalue1+180)%360))
    gensecrect = gensechand.get_rect()
    gensecrect.center = secrect.center

    screen.blit(gensechand, gensecrect)

    currenttime = datetime.datetime.now()
    secvalue1 = currenttime.second
    minvalue1 = currenttime.minute

    pygame.display.update()
    clock.tick(fps)

pygame.quit()