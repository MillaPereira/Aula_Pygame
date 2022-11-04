import sys, pygame
from window import Window

pygame.init()

win = Window(750, 650, (255,129,37))

screen = pygame.display.set_mode(win.get_size())
pygame.display.set_caption("Gaminho")

def tela_dia():
    # background
    background = pygame.image.load('assets/sky.png')
    background = pygame.transform.scale (background, (750,650))
    rect_background = background.get_rect()
    rect_background.center = (375,325)

    screen.blit(background, rect_background)

    # nuvens
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

    # botão
    botao_noite = pygame.image.load('assets/noite-play.png')
    botao_noite = pygame.transform.scale(botao_noite, (120,58))
    rect_botao_noite = botao_noite.get_rect()
    rect_botao_noite.center = (375,325)

    screen.blit(botao_noite, rect_botao_noite)

    pygame.display.update()

def tela_noite():
    # background
    background = pygame.image.load('assets/noite.jpg')
    background = pygame.transform.scale (background, (750,650))
    rect_background = background.get_rect()
    rect_background.center = (375,325)

    screen.blit(background, rect_background)

    # botão
    botao_dia = pygame.image.load('assets/dia-play.png')
    botao_dia = pygame.transform.scale(botao_dia, (120,58))
    rect_botao_dia = botao_dia.get_rect()
    rect_botao_dia.center = (375,325)

    screen.blit(botao_dia, rect_botao_dia)

    pygame.display.update()

tela_dia()
dia = True

clock = pygame.time.Clock()

while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN: 
            if (win.get_width()/2)-60 <= mouse[0] <= (win.get_width()/2)+60 and (win.get_height()/2) - 29 <= mouse[1] <= (win.get_height()/2)+29:
                if dia == True:    
                    tela_noite()
                    dia = False
                elif  dia == False:
                    tela_dia()
                    dia = True     

    mouse = pygame.mouse.get_pos() 
    
    clock.tick(60)         

    
