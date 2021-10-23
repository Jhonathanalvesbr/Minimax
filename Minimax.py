from Personagem import Personagem
from No import No
import math
import copy
import sys
sys.setrecursionlimit(10**6)

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
    return heuris+len(personagem)

def minimax(no, jogada, alpha, beta): 
    if len(no.player) == 0:
        return heuristica(no.playerInimigo)

    if len(no.playerInimigo) == 0:
        return -heuristica(no.player)
    
    if (jogada == True):
        best = -math.inf
        for i in no.playerInimigo:
            for p in no.player:
                p.vida -= i.ataque
                novoFilho = no.add_child()
                p.vida += i.ataque
                novoFilho.id.append(i)
                novoFilho.id.append(p)
                novoFilho.valor = no.valor = -math.inf
                novoFilho.valor = no.valor = max(no.valor, minimax(novoFilho, False, alpha, beta))
                best = max(best, novoFilho.valor)
                alpha = max(alpha, best)
                if (beta <= alpha):
                    break
        return best
    else:
        best = math.inf
        for p in no.player:
            for i in no.playerInimigo:
                i.vida -= p.ataque
                novoFilho = no.add_child()
                i.vida += p.ataque
                novoFilho.id.append(p)
                novoFilho.id.append(i)
                novoFilho.valor = no.valor = math.inf
                novoFilho.valor = no.valor = min(no.valor, minimax(novoFilho, True, alpha, beta))
                best = min(best, novoFilho.valor)
                beta = min(beta, best)
                if (beta <= alpha):
                        break
        return best
        


player[1].ataque = 3

playerInimigo[1].ataque = 3
        
no = No(None, player, playerInimigo,0)

x  = 0
print(minimax(no, True, -math.inf, math.inf))
for k in no.filho:
    print(str(x) + " : " + str(k.valor))
    x+=1

