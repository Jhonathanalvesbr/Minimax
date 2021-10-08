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
        x = 0
        for p in no.player:
            y = 0
            for i in no.playerInimigo:
                filho = No(player, playerInimigo, x, y)
                filho.altura = no.altura + 1
                filho.parente = no
    else:
         x = 0
         for i in no.playerInimigo:
            y = 0
            for p in no.player:
                filho = No(player, playerInimigo, x, y)
                filho.altura = no.altura + 1
                filho.parente = no
                y += 1
            x += 1

    jogada = not jogada


no = No()
no.altura = 0
no.player = player
no.playerInimigo = playerInimigo

print(minimax(no, True))
