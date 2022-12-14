import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [5, 5]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("assets/ball.png")
ball = pygame.transform.scale (ball, (20,20)) # diminui a imagem
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.K_ESCAPE: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width: # Checa se a imagem saiu da tela
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.update()