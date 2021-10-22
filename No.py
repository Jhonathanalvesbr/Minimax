from Personagem import Personagem
import copy

class No:
    def __init__(self, pai, player, playerInimigo, altura):
        self.pai = pai
        self.player = player
        self.playerInimigo = playerInimigo
        self.altura = altura
        self.filho = []

    heuristica = 0
    id = 0
    valor = 0

    def remover(self,personagem):
        for k in personagem:
            if(k.vida == 0):
                personagem.remove(k)
        return personagem

    def add_child(self):
        child = No(self, self.remover(copy.deepcopy(self.player)), self.remover(copy.deepcopy(self.playerInimigo)), self.altura)
        child.altura += 1
        self.filho.append(child)
        if(len(self.filho) >= 15):
            exit()
        return child