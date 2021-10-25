import pygame



class Personagem(pygame.sprite.Sprite):
    def sprite(self, sprite):
        self.tamanhoTela = 600
        self.sprites = sprite
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.angle = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = 100,100
        self.seguir = False
        self.mover = 0 
        self.movimento = []
        self.velocidade = 0.5
        self.tamanho = 0
        self.caminhar = False
        self.desX = None
        self.desY = None
        self.id = 0
        self.find = -1
        
        for i in range(len(self.sprites)):
            self.image = self.sprites[i]
            self.image = pygame.transform.rotate(self.image,200)
            
    def update(self, janela):
        if(self.id == 1 and self.caminhar == True):
            self.image = self.sprites[0]
            self.image = pygame.transform.scale(self.image,(int(self.tamanhoTela/25)*1,int(self.tamanhoTela/25)*1))
            self.image = pygame.transform.rotate(self.image,self.angle)
            return
        if(self.id == -1 and self.seguir == False):
            self.image = self.sprites[0]
            self.image = pygame.transform.scale(self.image,(int(self.tamanhoTela/25)*1,int(self.tamanhoTela/25)*1))
            self.image = pygame.transform.rotate(self.image,self.angle)
        elif(self.id == -1 and self.find == 1):
            self.image = self.sprites[0]
            self.image = pygame.transform.scale(self.image,(int(self.tamanhoTela/25)*1,int(self.tamanhoTela/25)*1))
            self.image = pygame.transform.rotate(self.image,self.angle)
        
        elif(self.id != -1):
            self.atual = self.atual + 0.005
            if self.atual >= len(self.sprites):
                self.atual = 0
            
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image,(int(self.tamanhoTela/25)*1,int(self.tamanhoTela/25)*1))
            self.image = pygame.transform.rotate(self.image,self.angle)
        else:
            self.image = pygame.transform.scale(self.image,(int(self.tamanhoTela/25)*1,int(self.tamanhoTela/25)*1))
            return
        
    def angulo(self,angle):
        self.angle = angle

    def cima(self, passo):
        self.rect.move_ip(0,-passo)

    def baixo(self,passo):
        self.rect.move_ip(0,passo)

    def esquerda(self,passo):
        self.rect.move_ip(-passo,0)

    def direita(self,passo):
        self.rect.move_ip(passo,0)