from Personagem import Personagem



class No:
    pai = []
    altura = None
    alpah = 1
    beta = -1
    heuristica = None
    filho = []
    
    def __init__(self, player, playerInimigo, idPlayer, idPlayerInimigo):
        self.player = player
        self.playerInimigo = playerInimigo
        self.id = []
        self.id.append(idPlayer)
        self.id.append(idPlayerInimigo)

    def __init__(self):
        self.player = []
        self.playerInimigo = []