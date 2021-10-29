import pygame
from Personagem import Personagem
import copy

class Personagem(pygame.sprite.Sprite):

    def sprite(self, sprite):
        self.personagem = None
        self.tamanhoTela = 600
        self.sprites = sprite
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.angle = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = 50,50
        self.rect[2] = 50
        self.rect[3] = 50
        self.seguir = False
        self.mover = 0 
        self.movimento = []
        self.velocidade = 0.5
        self.tamanho = 0
        self.caminhar = False
        self.desX = None
        self.desY = None
        self.id = 0
        self.find = []
        self.x = None
        self.y = None
        self.jogador = None
        self.spriteVida = None
        self.posicaoVida = None
        self.spriteCaregarVida = None
        self.posicaoCarregar = None
        self.spriteRed = None
        self.posicaoRed = None
        self.ataque = 0
        self.vida = 1
        self.vidaTotal = 1
        self.fim = 0
        
        
        for i in range(len(self.sprites)):
            self.image = self.sprites[i]
            self.image = pygame.transform.rotate(self.image,200)
            
    def update(self, janela):
        cemVida = (25 * self.vida) / self.vidaTotal
        if(cemVida <= 0):
            cemVida = 1



        self.posicaoVida = copy.deepcopy(self.rect)
        self.posicaoRed = copy.deepcopy(self.rect)
        self.posicaoCarregar = copy.deepcopy(self.rect)

        self.spriteCaregarVida = pygame.transform.scale(self.spriteCaregarVida,(int(cemVida),int(5)))
        self.posicaoCarregar.x += 1
        self.posicaoRed.x += 1
        
        janela.blit(self.spriteVida,self.posicaoVida)
        janela.blit(self.spriteRed,self.posicaoRed)
        janela.blit(self.spriteCaregarVida,self.posicaoCarregar)
        

        
        if(self.id != -1):
            self.atual = self.atual + 0.005
            if self.atual >= len(self.sprites):
                self.atual = 0
            
            self.image = self.sprites[int(self.atual)]
            if(self.jogador):
                self.image = pygame.transform.scale(self.image,(int(self.tamanhoTela/12)*1,int(self.tamanhoTela/8)*1))
            else:
                self.angle = -180
                self.image = pygame.transform.flip(self.image , 1, 0)
                self.image = pygame.transform.scale(self.image,(int(self.tamanhoTela/25)*1,int(self.tamanhoTela/25)*1))

            

        
    def angulo(self,angle):
        self.angle = angle

    def cima(self, passo):
        self.rect.move_ip(0,passo)

    def baixo(self,passo):
        self.rect.move_ip(0,-passo)

    def esquerda(self,passo):
        self.rect.move_ip(passo,0)

    def direita(self,passo):
        self.rect.move_ip(*-passo,0)