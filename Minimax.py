import copy
from Personagem import Personagem
from No import No
import math

playerInimigo = []
player = []
no = []

for i in range(3):
    aux = Personagem()
    aux.id = i
    playerInimigo.append(aux)
aux = Personagem()
aux.id = 1
player.append(aux)

a = 0
def minimax(no, jogada, alpha, beta):
    global a
    if (len(no.player) == 0):
        return -no.altura

    if (len(no.playerInimigo) == 0):
        return no.altura

    
    if (jogada == True):
        best = -100
        filhos = []
        for p in no.player:
            for i in no.playerInimigo:
                if(i.vida > 0):
                    novoFilho = No()
                    novoFilho.pai = no
                    filhos.append(novoFilho)
                    playerCopy = Personagem
                    playerCopy.vida = p.vida * 1
                    playerCopy.ataque = p.ataque * 1
                    playerInimigoCopy = Personagem
                    playerInimigoCopy.vida = i.vida * 1
                    playerInimigoCopy.ataque = i.ataque * 1
                    novoFilho.player.append(playerCopy)
                    novoFilho.playerInimigo.append(playerInimigoCopy)
                    novoFilho.altura = no.altura + 1
                    playerInimigoCopy.vida -= playerCopy.ataque
                    if (playerInimigoCopy.vida <= 0):
                        novoFilho.playerInimigo.remove(playerInimigoCopy)

                    novoFilho.valor = no.valor = -100
                    jogada = False
                    a += 1
                    novoFilho.valor = no.valor = max(no.valor, minimax(novoFilho, jogada, alpha, beta))
                    best = max(best, novoFilho.valor)
                    alpha = max(alpha, best)
                    
                    if (beta <= alpha):
                        break
        no.filho = filhos
        return best
    else:
        filhos = []
        best = 100
        for i in no.playerInimigo:
            for p in no.player:
                if(p.vida > 0):
                    novoFilho = No()
                    novoFilho.pai = no
                    filhos.append(novoFilho)
                    playerCopy = Personagem
                    playerCopy.vida = p.vida * 1
                    playerCopy.ataque = p.ataque * 1
                    playerInimigoCopy = Personagem
                    playerInimigoCopy.vida = i.vida * 1
                    playerInimigoCopy.ataque = i.ataque * 1
                    novoFilho.player.append(playerCopy)
                    novoFilho.playerInimigo.append(playerInimigoCopy)
                    novoFilho.altura = no.altura + 1
                    playerCopy.vida -= playerInimigoCopy.ataque
                    if (playerCopy.vida <= 0):
                        novoFilho.player.remove(playerCopy)

                    novoFilho.valor = no.valor = 100
                    jogada = True
                    a += 1
                    novoFilho.valor = no.valor = min(no.valor, minimax(novoFilho, jogada, alpha, beta))
                    best = min(best, novoFilho.valor)
                    beta = min(beta, best)
 
                    if (beta <= alpha):
                        break
        no.filho = filhos
        return best

no = No()
no.player = player
no.playerInimigo = playerInimigo
no.altura = 0

print(minimax(no, True, -100, 100))
