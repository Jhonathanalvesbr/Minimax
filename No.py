from math import inf
from Personagem import Personagem

def copy(player):

    auxPlayer = []
    for p in player:
        aux = Personagem()
        aux.vida = p.vida
        auxPlayer.append(aux)
    
    return auxPlayer

class No:
    parente = None
    altura = None
    alpah = inf
    beta = -inf
    heuristica = None

    def __init__(self, player, playerInimigo):
        self.player = copy(player)
        self.playerInimigo = copy(playerInimigo)
        self.id = []
        self.id.append(player.id)
        self.id.append(playerInimigo.id)