import math
from random import randint
from enum import Enum

# Representa um asteróide
class TAsteroide:
    def __init__(self, nome, x, y, raio):
        self.nome = nome
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = self.setCor(raio)
        self.x_velocidade = self.getVelocidade()
        self.y_velocidade = self.getVelocidade()

    # checa colisão entre este asteroide e outro
    def colisao(self, ast2):
        distancia =  math.sqrt( ((self.x-ast2.x)**2)+((self.y-ast2.y)**2) )
        if (self.raio + ast2.raio) >= distancia:
            return True
        else:
            return False
    
    # checa colisao com todos os asteroides da lista
    def checaColisoes(self, asteroides):
        for asteroide in asteroides:
            if asteroide != self:
                if self.colisao(asteroide):
                    print("COLISÃO! %s e %s" %(self.__str__(), asteroide.__str__()))
                    self.inverterVelocidade()

    # Retorna uma tupla que representa a cor em RGB
    def getCorEmRgb(self):
        if self.cor == TCor.VERMELHO:
            return (255, 0, 0)
        elif self.cor == TCor.VERDE:
            return (0, 255, 0)
        else:
            return (0, 0, 255)
    
    # Atribui um tipo enumerado para o campo cor baseado no tamanho do raio
    def setCor(self, raio):
        if raio == 10:
            return TCor.VERMELHO
        elif raio == 20:
            return TCor.VERDE
        else:
            return TCor.AZUL 

    def getVelocidade(self):
        v = randint(-5, 5)
        while v == 0:
            v = randint(-5, 5)
        return v

    def inverterVelocidade(self):
        self.inverterXVelocidade()
        self.inverterYVelocidade()

    def inverterXVelocidade(self):
        self.x_velocidade *= -1

    def inverterYVelocidade(self):
        self.y_velocidade *= -1

    def mover(self):
        self.x += self.x_velocidade
        self.y += self.y_velocidade

    def checaLimiteTela(self, tela):
        if self.x not in range(0, tela.get_width()):
            self.inverterXVelocidade()
        if self.y not in range(0, tela.get_height()):
            self.inverterYVelocidade()

    def __str__(self):
        return "[%s cor: %s]" %(self.nome, self.cor.name)

# Enum para as cores
# Cada um dos 3 possíveis raios que um asteroide pode ter são associados a uma cor
class TCor(Enum):
    VERMELHO = 10
    VERDE = 20
    AZUL = 30

    
