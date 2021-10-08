from math import inf

class No:
    familia = None
    altura = None
    alpah = inf
    beta = -inf

    def __init__(self, player, playerInimigo):
        self.player = player
        self.playerInimigo = playerInimigo
        self.id = []
        self.id.append(player.id)
        self.id.append(playerInimigo.id)