import pygame

class Personagem(pygame.sprite.Sprite):
    def sprite(self, sprite):
        self.tamanhoTela = 600
        self.sprites = sprite
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = 50,50

                   
    def update(self, janela):
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image,(int(self.tamanhoTela/25)*1,int(self.tamanhoTela/25)*1))
            

