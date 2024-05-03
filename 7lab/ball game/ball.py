import pygame
pygame.init()

W, H = 600, 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)

sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Moving Red Ball")

clock = pygame.time.Clock()
FPS = 60

x = W // 2
y = H // 2
radius = 25

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = max(radius, x -20)
    if keys[pygame.K_RIGHT]:
        x = min(W - radius, x +20)
    if keys[pygame.K_UP]:
        y = max(radius, y - 20)
    if keys[pygame.K_DOWN]:
        y = min(H - radius, y + 20)

    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x, y), radius)
    pygame.display.update()

    clock.tick(FPS)
