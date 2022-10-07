import sys, pygame
from window import Window

pygame.init()

win = Window(600, 600, (255,129,37))

screen = pygame.display.set_mode(win.get_size())
pygame.display.set_caption("Gaminho")

ball = pygame.image.load("assets/ball.png")
ball = pygame.transform.scale (ball, (20,20)) # diminui a imagem
ballrect = ball.get_rect()

screen.fill(win.get_color())

pygame.display.update()

pos = [300,300]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()
            elif event.key == pygame.K_LEFT: pos[0] = pos[0] + -10
            elif event.key == pygame.K_UP: pos[1] = pos[1] -10
            elif event.key == pygame.K_DOWN: pos[1] = pos[1] + 10
            elif event.key == pygame.K_RIGHT: pos[0] = pos[0] + 10

    ballrect.center = (pos[0],pos[1])

    if ballrect.left < 0 or ballrect.right > win.get_width(): # Checa se a imagem saiu da tela
        ballrect.center = (300,300)
    if ballrect.top < 0 or ballrect.bottom > win.get_height():
        ballrect.center = (300,300)
    
    screen.fill(win.get_color())
    screen.blit(ball, ballrect)
    pygame.display.update()




    
