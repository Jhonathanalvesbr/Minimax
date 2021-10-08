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


def minimax(no, jogada):
    if(len(no.player) == 0):
        no.heuristica = no.parente.altura + 1
        return 
    if(len(no.playerInimigo) == 0):
        no.heuristica = no.parente.altura + 1
        return 
    
    if(jogada):
        for p in no.player:
            for i in no.playerInimigo:
                aux = No()
                aux.altura = no.altura + 1
                aux.parente = no
    else:
         for i in no.playerInimigo:
            for p in no.player:
                aux = No()
                aux.altura = no.altura + 1
                aux.parente = no

    jogada = not jogada


no = No()
no.altura = 0
no.player = player
no.playerInimigo = playerInimigo

print(minimax(no, True))
