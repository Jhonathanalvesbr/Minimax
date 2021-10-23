import pygame



class sprite(pygame.sprite.Sprite):
    jogador = True
    spriteVida = pygame.image.load("C:\\Users\\jhona\\Desktop\\Minimax\\Minimax\\pacote\\barra\\Loading Bar Background.png")
    spriteVida = pygame.transform.scale(spriteVida,(int(80),int(20)))
    posicaoVida = spriteVida.get_rect(midleft=(90, 20))
    spriteCaregar = pygame.image.load("C:\\Users\\jhona\\Desktop\\Minimax\\Minimax\\pacote\\barra\\Loading Bar Green.png")
    spriteCaregar = pygame.transform.scale(spriteCaregar,(int(80),int(20)))
    posicaoCarregar = spriteCaregar.get_rect(midleft=(90, 20))
    

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
    
    def update(self, janela):
        self.atual += 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        if(self.jogador == False):
            self.image =  pygame.transform.flip(self.image , 1, 0)
            self.posicaoVida = self.spriteVida.get_rect(midleft=(self.rect.x-80, self.rect.y))
            cem = (74 * self.personagem.vida) / self.vidaTotal

            self.spriteCaregar = pygame.transform.scale(self.spriteCaregar,(int(cem),int(20)))
            self.posicaoCarregar = self.spriteCaregar.get_rect(midleft=(self.rect.x-77, self.rect.y))
        else:
            cem = (74 * self.personagem.vida) / self.vidaTotal
            self.posicaoVida = self.spriteVida.get_rect(midleft=(self.rect.x+100, self.rect.y))
            self.spriteCaregar = pygame.transform.scale(self.spriteCaregar,(int(cem),int(20)))
            self.posicaoCarregar = self.spriteCaregar.get_rect(midleft=(self.rect.x+103, self.rect.y))

        

        janela.blit(self.spriteVida,self.posicaoVida)
        janela.blit(self.spriteCaregar,self.posicaoCarregar)
        

