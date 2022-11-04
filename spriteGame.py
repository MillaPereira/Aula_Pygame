import pygame
import random
from window import Window
 
# Definindo as cores
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

# criando a classe Bloco herdando a classe sprite nativa do pygame
class Bloco(pygame.sprite.Sprite): 
    def __init__(self, color, width, height): 
        # construtor da classe pai
        super().__init__()
 
        # Cria uma imagem do bloco e preenche com a cor passa para o construtor
        # Tambem poderia ser uma imagem
        # self.image = pygame.image.load(caminhoImagem)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Define o retangulo do sprite como sendo o retangulo da imagem criada.
        self.rect = self.image.get_rect()
 
# Iniciando o pygame
pygame.init()
 
# Iniciando a tela
win = Window(750, 650, (255,129,37))

screen = pygame.display.set_mode(win.get_size())
pygame.display.set_caption("Gaminho")
 
# Lista com todos os blocos
lista_blocos = pygame.sprite.Group()
 
# Lista com todos os sprites
lista_todos_sprites = pygame.sprite.Group()


# Gerando os blocos "inimigos" e adicionando nas listas
for i in range(50):
    # chamando o construtor da classe Bloco
    bloco = Bloco(BLACK, 20, 15)
 
    # Coloca o bloca em uma posição aleatória dentro da tela
    bloco.rect.x = random.randrange(win.get_width())
    bloco.rect.y = random.randrange(win.get_height())
 
    # Adiciona o bloco na lista
    lista_blocos.add(bloco)
    lista_todos_sprites.add(bloco)
 
# Cria o bloco de jogador
jogador = Bloco(RED, 20, 15)
lista_todos_sprites.add(jogador)
 
# O jogo acaba quando fimDoJo = True
fimDoJogo = False
 
# Usado para definir a que taxa a tela atualiza
clock = pygame.time.Clock()
 
pontuacao = 0
 
# -------- Game Loop -----------
while not fimDoJogo:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            fimDoJogo = True
 
    # Limpa a tela
    screen.fill(WHITE)
    
    # Verifica se alguma seta foi apertada e muda a posição do jogador em caso positivo
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        jogador.rect.x -= 2
    if keys[pygame.K_RIGHT]:
        jogador.rect.x += 2
    if keys[pygame.K_UP]:
        jogador.rect.y -= 2
    if keys[pygame.K_DOWN]:
        jogador.rect.y += 2
 
    # Verifica se o bloco jogadr colidiu com algum outro sprite
    lista_colisoes = pygame.sprite.spritecollide(jogador, lista_blocos, True)
 
    # Checa a lista de colisões
    for block in lista_colisoes:
        pontuacao += 1
        print(pontuacao)

    if pontuacao == 50:
        done = True
 
    # Desenha todos os sprites
    lista_todos_sprites.draw(screen)
 
    # Atualiza a tela
    pygame.display.flip()
 
    # Limita a atualização da tela a uma taxa de 60 fps
    clock.tick(60)
 
pygame.quit()