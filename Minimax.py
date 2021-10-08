from Personagem import Personagem
from No import No

playerInimigo = []
player = []
no = []

for i in range(3):
    aux = Personagem()
    playerInimigo.append(aux)
    aux = Personagem()
    player.append(aux)

def copy(player):

    auxPlayer = []
    for p in player:
        aux = Personagem()
        aux.vida = p.vida
        auxPlayer.append(aux)
    
    return auxPlayer

def minimax(player, playerInimigo, jogada):
    if(len(player) == 0):
        return 1
    if(len(playerInimigo) == 0):
        return -1
    
    player = copy(player)
    playerInimigo = copy(playerInimigo)

    if(jogada):
        for p in player:
            for i in playerInimigo:
                if(i.vida <= 0):
                    playerInimigo.remove(i)
                i.vida -= p.ataque
            return minimax(player, playerInimigo, True)
    else:
         for i in playerInimigo:
            for p in player:
                if(p.vida <= 0):
                    player.remove(p)
                p.vida -= i.ataque
            return minimax(player, playerInimigo, False)
    jogada = not jogada



print(minimax(player, playerInimigo, False))

