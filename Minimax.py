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
    if len(no.player) == 0:
        return -no.altura

    if len(no.playerInimigo) == 0:
        return no.altura

    
    print(jogada)
    if jogada == True:
        best = -math.inf
        filhos = []
        playerCopy = []
        playerInimigoCopy = []
        for p in no.player:
            for i in no.playerInimigo:
                if i.vida > 0:
                    novoFilho = No
                    novoFilho.pai = no
                    filhos.append(novoFilho)

                    i.vida -= p.ataque
                    for k in no.player:
                        playerCopy.append(copy.deepcopy(k))
                    for k in no.playerInimigo:
                        if k.vida > 0:
                            playerInimigoCopy.append(copy.deepcopy(k))
                    
                    novoFilho.player = playerCopy
                    novoFilho.PlayerInimigo = playerInimigoCopy
                    print("Tam: " + str(len(novoFilho.player)))
                    print("Tam: " + str(len(novoFilho.PlayerInimigo)))
                    i.vida += p.ataque
                    novoFilho.altura = no.altura + 1
                    novoFilho.valor = no.valor = -math.inf
                    jogada = not jogada
                    a += 1
                    print(11)
                    
                    novoFilho.valor = no.valor = max(no.valor, minimax(novoFilho, jogada, alpha, beta))
                    best = max(best, novoFilho.valor)
                    alpha = max(alpha, best)

                    if beta <= alpha:
                        break

        no.filho = filhos
        return best

    else:
        filhos = []
        best = math.inf
        playerCopy = []
        playerInimigoCopy = []
        for i in no.playerInimigo:
            for p in no.player:
                if p.vida > 0:
                    novoFilho = No
                    novoFilho.pai = no
                    filhos.append(novoFilho)

                    p.vida -= i.ataque
                    for k in no.player:
                        if k.vida > 0:
                            playerCopy.append(copy.deepcopy(k))
                    for k in no.playerInimigo:
                        playerInimigoCopy.append(copy.deepcopy(k))

                    novoFilho.player = playerCopy
                    novoFilho.PlayerInimigo = playerInimigoCopy
                    p.vida += i.ataque
                    novoFilho.altura = no.altura + 1
                    novoFilho.valor = no.valor = math.inf
                    jogada = not jogada
                    a += 1
                    print(22)
                    
                    novoFilho.valor = no.valor = min(no.valor, minimax(novoFilho, jogada, alpha, beta))
                    best = min(best, novoFilho.valor)
                    beta = min(beta, best)

                    if beta <= alpha:
                        break

        no.filho = filhos
        return best


no = No()
no.player = player
no.playerInimigo = playerInimigo
no.altura = 0

print(minimax(no, True, -math.inf, math.inf))
print(len(no.filho))
print(a)