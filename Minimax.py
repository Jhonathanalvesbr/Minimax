from Personagem import Personagem
from No import No
import math
import copy

playerInimigo = []
player = []
no = []

for i in range(3):
    aux = Personagem()
    aux.id = i
    aux.vida = 1
    playerInimigo.append(aux)
    aux = Personagem()
    aux.id = i
    aux.vida = 1
    player.append(aux)

def heuristica(personagem):
    heuris = 0
    for k in personagem:
        heuris += k.ataque
        heuris += k.vida
    return heuris+len(personagem)
a = 0
def minimax(no, jogada, alpha, beta):
    global a
    a += 1
    if len(no.player) == 0:
        return no.altura

    if len(no.playerInimigo) == 0:
        return -heuristica(no.player)

    if (jogada):
            best = -math.inf
            i = 0
            while i < len(no.playerInimigo):
                j = 0
                while j < len(no.player):
                    novoFilho = no.add_child()
                    
                    k = 0
                    while k < len(no.player):
                        aux = copy.deepcopy(no.player[k])
                        novoFilho.player.append(aux)
                        k += 1
                    k = 0
                    while k < len(no.playerInimigo):
                        aux = copy.deepcopy(no.playerInimigo[k])
                        novoFilho.playerInimigo.append(aux)
                        k += 1

                    novoFilho.player[j].vida -= no.playerInimigo[i].ataque
                    if (novoFilho.player[j].vida <= 0):
                        novoFilho.player.remove(j)

                    novoFilho.valor = no.valor = -math.inf

                    novoFilho.valor = no.valor = max(no.valor, minimax(novoFilho, false, alpha, beta))
                    best = max(best, novoFilho.valor)
                    alpha = max(alpha, best)
                    j += 1
                    if (beta <= alpha):
                        break
                i += 1
            return best
    else:
            best = math.inf;
            i = 0
            while i < len(no.player):
                j = 0
                while j < len(no.playerInimigo):
                    novoFilho = no.add_child()

                    k = 0
                    while k < len(no.player):
                        aux = copy.deepcopy(no.player.get(k))
                        novoFilho.player.append(aux)
                        k += 1
                    k = 0
                    while k < len(no.playerInimigo):
                        aux = copy.deepcopy(no.playerInimigo.get(k))
                        novoFilho.playerInimigo.append(aux)
                        k += 1

                    novoFilho.playerInimigo[j].vida -= no.player.get[i].ataque
                    if (novoFilho.playerInimigo.get[j].vida <= 0):
                        novoFilho.playerInimigo.remove(j)
                    
                    novoFilho.valor = no.valor = math.inf

                    novoFilho.valor = no.valor = min(no.valor, minimax(novoFilho, true, alpha, beta))
                    best = min(best, novoFilho.valor)
                    beta = min(beta, best)
                    j += 1
                    if (beta <= alpha):
                        break
                i += 1

                
            
            return best;
        


player[1].ataque = 3
playerInimigo[1].ataque = 3
        
no = No(None, player, playerInimigo,0)

x  = 0
print(minimax(no, True, -math.inf, math.inf))
for k in no.filho:
    print(str(x) + " : " + str(k.valor))
    x+=1
