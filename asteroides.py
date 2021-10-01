import math
import pygame
from pygame.locals import *
import random
from TAsteroide import TAsteroide

# Gera um asteroide com valores aleatorios
# Há apenas 3 valores possíveis para o raio, 10, 20 e 30, e este
# tamanho irá posteriormente influenciar na cor do asteroide.
def gerarAsteroide(nome):
    x = random.randint(0, 600)
    y = random.randint(0, 400)
    raio = random.randrange(10, 31, 10)
    return TAsteroide(nome, x, y, raio)

def desenharAsteroide(asteroide):
    x = asteroide.x
    y = asteroide.y
    raio = asteroide.raio
    corRgb = asteroide.getCorEmRgb()
    pygame.draw.circle(screen, corRgb, (x, y), raio)

pygame.init()

screen = pygame.display.set_mode((600,400))

clock = pygame.time.Clock()

asteroides = []

for i in range (0, 10):
    nome = "Asteroide %i" %(i)
    asteroides.append(gerarAsteroide(nome))

while True:
    screen.fill((10,10,10))

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    
    for a in asteroides:
        desenharAsteroide(a)
        a.mover()
        a.checaColisoes(asteroides)
        a.checaLimiteTela(screen)
        
    pygame.display.update()
