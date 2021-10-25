import pygame
import os

class sprite(pygame.sprite.Sprite):
    jogador = True
    spriteVida = pygame.image.load(os.getcwd()+"\\pacote\\barra\\Loading Bar Background.png")
    spriteVida = pygame.transform.scale(spriteVida,(int(80),int(20)))
    posicaoVida = spriteVida.get_rect(midleft=(90, 20))

    spriteCaregarVida = pygame.image.load(os.getcwd()+"\\pacote\\barra\\Loading Bar Green.png")
    spriteCaregarVida = pygame.transform.scale(spriteCaregarVida,(int(80),int(20)))
    posicaoCarregar = spriteCaregarVida.get_rect(midleft=(90, 20))

    spriteRed = pygame.image.load(os.getcwd()+"\\pacote\\barra\\Barra_Vermelho.png")
    spriteRed = pygame.transform.scale(spriteRed,(int(80),int(20)))
    posicaoRed = spriteRed.get_rect(midleft=(90, 20))

    spriteAzul = pygame.image.load(os.getcwd()+"\\pacote\\barra\\Barra_Azul.png")
    spriteAzul = pygame.transform.scale(spriteAzul,(int(80),int(20)))
    posicaoAzul = spriteAzul.get_rect(midleft=(90, 20))

    spriteCaregarVelocidade = pygame.image.load(os.getcwd()+"\\pacote\\barra\\Loading Bar Background.png")
    spriteCaregarVelocidade = pygame.transform.scale(spriteCaregarVelocidade,(int(80),int(20)))
    posicaoCarregarVelocidade = spriteCaregarVelocidade.get_rect(midleft=(90, 20))
    

    def updateSprite(self,sprite):
        self.sprites = sprite
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.angle = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = 100,100
        self.nome = ""
        self.personagem = None
        self.vidaTotal = 0
        self.velocidadeTotal = 0
    
    def update(self, janela):
        self.atual += 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        if(self.jogador == False):
            cemVida = (74 * self.personagem.vida) / self.vidaTotal
            if(cemVida <= 0):
                cemVida = 1
            cemVelocidade = (74 * self.personagem.velocidade) / self.velocidadeTotal
            if(cemVelocidade <= 0):
                cemVelocidade = 1

            self.posicaoAzul = self.spriteAzul.get_rect(midleft=(self.rect.x-80, self.rect.y+25))
            self.spriteAzul = pygame.transform.scale(self.spriteAzul,(int(cemVelocidade),int(20)))
            self.posicaoCarregarVelocidade = self.spriteAzul.get_rect(midleft=(self.rect.x-83, self.rect.y+25))

            self.posicaoVida = self.spriteVida.get_rect(midleft=(self.rect.x-83, self.rect.y))
            self.spriteCaregarVida = pygame.transform.scale(self.spriteCaregarVida,(int(cemVida),int(20)))
            self.posicaoCarregar = self.spriteCaregarVida.get_rect(midleft=(self.rect.x-80, self.rect.y))


            self.image =  pygame.transform.flip(self.image , 1, 0)

            self.posicaoRed= self.spriteRed.get_rect(midleft=(self.rect.x-80, self.rect.y))
            self.spriteRed = pygame.transform.scale(self.spriteRed,(int(75),int(20)))
        else:
            cemVida = (74 * self.personagem.vida) / self.vidaTotal
            if(cemVida <= 0):
                cemVida = 1
            cemVelocidade = (74 * self.personagem.velocidade) / self.velocidadeTotal
            if(cemVelocidade <= 0):
                cemVelocidade = 1
            
            self.posicaoRed = self.spriteRed.get_rect(midleft=(self.rect.x+100, self.rect.y))
            self.spriteRed = pygame.transform.scale(self.spriteRed,(int(78),int(20)))

            self.posicaoAzul = self.spriteAzul.get_rect(midleft=(self.rect.x+102, self.rect.y+25))
            self.spriteAzul = pygame.transform.scale(self.spriteAzul,(int(cemVelocidade),int(20)))
            self.posicaoCarregarVelocidade = self.spriteAzul.get_rect(midleft=(self.rect.x+100, self.rect.y+25))

            self.posicaoVida = self.spriteVida.get_rect(midleft=(self.rect.x+100, self.rect.y))
            self.spriteCaregarVida = pygame.transform.scale(self.spriteCaregarVida,(int(cemVida),int(20)))
            self.posicaoCarregar = self.spriteCaregarVida.get_rect(midleft=(self.rect.x+103, self.rect.y))

        self.image = pygame.transform.scale(self.image,(int(120),int(120)))

        janela.blit(self.spriteVida,self.posicaoVida)
        janela.blit(self.spriteCaregarVelocidade,self.posicaoCarregarVelocidade)
        janela.blit(self.spriteRed,self.posicaoRed)
        janela.blit(self.spriteAzul,self.posicaoAzul)
        janela.blit(self.spriteCaregarVida,self.posicaoCarregar)
        

