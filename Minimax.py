from Personagem import Personagem
from No import No

playerInimigo = []
player = []
no = []

for i in range(3):
    aux = Personagem()
    aux.id = i
    playerInimigo.append(aux)
    aux = Personagem()
    aux.id = i
    player.append(aux)

def copy(player):
    if(len(player) == 0):
        return None

    auxPlayer = []
    for p in player:
        aux = Personagem()
        aux.vida = p.vida
        auxPlayer.append(aux)
    
    return auxPlayer

def minimax(no, jogada):
    if(len(no.player) == 0):
        #no.heuristica = no.parente.altura + 1
        return no
    if(len(no.playerInimigo) == 0):
        #no.heuristica = no.parente.altura + 1
        return no


    
    if(jogada):
        x = 0
        for p in no.player:
            y = 0
            for i in no.playerInimigo:
                if(i.vida == 0):
                    no.playerInimigo.remove(i)
                    y -= 1
                else:
                    auxPlayer = copy(player)
                    auxPlayerInimigo = copy(playerInimigo)
                    auxPlayerInimigo[y].vida -= 1
                    filho = No(auxPlayer, auxPlayerInimigo, x, y)
                    filho.altura = no.altura + 1
                    filho.pai = no
                    no.filho.append(filho)
                    print(auxPlayerInimigo[y].vida)
                    minimax(filho, True)
                    y += 1
            x += 1


    

no = No(player, playerInimigo, None, None)
no.altura = 0

print(minimax(no, True))
