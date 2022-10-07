import sys, pygame
from window import Window

pygame.init()

win = Window(750, 650, (255,129,37))

screen = pygame.display.set_mode(win.get_size())
pygame.display.set_caption("Gaminho")

def montar_cenario():
    # background
    background = pygame.image.load('assets/sky.png')
    background = pygame.transform.scale (background, (950,650))
    rect_background = background.get_rect()
    rect_background.center = (300,300)

    screen.blit(background, rect_background)

    # plataformas
    plataforma1 = pygame.image.load('assets/platform.png')
    rect_platform1 = plataforma1.get_rect()
    rect_platform1.center = (200,200)

    screen.blit(plataforma1, rect_platform1)

    plataforma2 = pygame.image.load('assets/platform.png')
    rect_platform2 = plataforma2.get_rect()
    rect_platform2.center = (700,400)

    screen.blit(plataforma2, rect_platform2)

    plataforma3 = pygame.image.load('assets/platform.png')
    rect_platform3 = plataforma3.get_rect()
    rect_platform3.center = (120,470)

    screen.blit(plataforma3, rect_platform3)

    plataforma4 = pygame.image.load('assets/platform.png')
    plataforma4 = pygame.transform.scale (plataforma4, (950,60))
    rect_platform4 = plataforma4.get_rect()
    rect_platform4.center = (475,650)

    screen.blit(plataforma4, rect_platform4)
    
    pygame.display.update()

temp = 0

montar_cenario()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()
            elif event.key == pygame.K_UP: temp = 1
            elif event.key == pygame.K_LEFT: temp = 1
            elif event.key == pygame.K_RIGHT: temp = 1
            elif event.key == pygame.K_DOWN: temp = 1


    
