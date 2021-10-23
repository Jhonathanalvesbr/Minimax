from Personagem import Personagem
import copy

class No:
    def __init__(self, pai, player, playerInimigo, altura):
        self.pai = pai
        self.player = player
        self.playerInimigo = playerInimigo
        self.altura = altura
        self.filho = []
        self.heuristica = 0
        self.id = []
        valor = 0

    def removerMorre(self,personagem):
        for k in personagem:
            if(k.vida <= 0):
                personagem.remove(k)
        return personagem

    def add_child(self):
        child = No(self, [], [], self.altura)
        child.altura += 1
        child.player = self.removerMorre(copy.deepcopy(self.player))
        child.playerInimigo = self.removerMorre(copy.deepcopy(self.playerInimigo))
        self.filho.append(child)
        return child