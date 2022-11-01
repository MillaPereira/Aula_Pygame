import sys, pygame
from window import Window

pygame.init()

win = Window(750, 650, (255,129,37))

screen = pygame.display.set_mode(win.get_size())
pygame.display.set_caption("Gaminho")

def tela_dia():
    # background
    background = pygame.image.load('assets/sky.png')
    background = pygame.transform.scale (background, (950,650))
    rect_background = background.get_rect()
    rect_background.center = (300,300)

    screen.blit(background, rect_background)

    # plataformas
    nuvem1 = pygame.image.load('assets/cloud.png')
    nuvem1 = pygame.transform.scale(nuvem1, (200,100))
    rect_nuvem1 = nuvem1.get_rect()
    rect_nuvem1.center = (200,200)

    screen.blit(nuvem1, rect_nuvem1)

    nuvem2 = pygame.image.load('assets/cloud.png')
    nuvem2 = pygame.transform.scale(nuvem2, (300,150))
    rect_nuvem2 = nuvem2.get_rect()
    rect_nuvem2.center = (550,400)

    screen.blit(nuvem2, rect_nuvem2)

    pygame.display.update()

tela_dia()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()
            elif event.key == pygame.K_UP: temp = 1
            elif event.key == pygame.K_LEFT: temp = 1
            elif event.key == pygame.K_RIGHT: temp = 1
            elif event.key == pygame.K_DOWN: temp = 1


    
