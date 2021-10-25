from PeronsagemSprite import sprite

class Personagem:
    def __init__(self):
        self.vida = 2
        self.ataque = 1
        self.level = 1
        self.velocidade = 1
        self.sprite = sprite()
        self.nome = ""

    def updateSprite(self, sprite, nome):
        self.nome = nome
        self.sprite.sprites = sprite
        self.sprite.atual = 0
        self.sprite.image = self.sprite.sprites[self.sprite.atual]
        self.sprite.angle = 0
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.topleft = 100,100
        self.sprite.personagem = self
        self.sprite.vidaTotal = self.vida
        self.sprite.velocidadeTotal = self.velocidade