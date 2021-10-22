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
    aux.id = i
    player.append(aux)

def heuristica(personagem):
    heuris = 0
    for k in personagem:
        heuris += k.ataque
        heuris += k.vida
    return heuris

def minimax(no, jogada, alpha, beta):
    if len(no.player) == 0:
        return heuristica(no.playerInimigo)

    if len(no.playerInimigo) == 0:
        return -heuristica(no.player)

    if jogada == True:
        best = -math.inf
        for p in no.playerInimigo:
            for i in no.player:
                if i.vida > 0:
                    i.vida -= p.ataque
                    novoFilho = no.add_child()                 
                    i.vida += p.ataque

                    novoFilho.valor = -math.inf
                    no.valor = -math.inf
                    
                    novoFilho.valor = no.valor = max(no.valor, minimax(novoFilho, False, alpha, beta))
                    best = max(best, novoFilho.valor)
                    alpha = max(alpha, best)
                    if (beta <= alpha):
                        break
        return best
    else:
        print(2)
        best = math.inf
        for i in no.player:
            for p in no.playerInimigo:
                if p.vida > 0:
                    i.vida -= p.ataque
                    novoFilho = no.add_child()                 
                    i.vida += p.ataque

                    novoFilho.valor = math.inf
                    no.valor = math.inf

                    novoFilho.valor = no.valor = min(no.valor, minimax(novoFilho, True, alpha, beta))
                    best = min(best, novoFilho.valor)
                    beta = min(beta, best)
                    if (beta <= alpha):
                        break
        return best

no = No(None, player, playerInimigo,0)

print(minimax(no, True, -math.inf, math.inf))
for k in no.filho:
    print(k.valor)
print("====================================")
for k in no.filho[0].filho:
    print(k.valor)

