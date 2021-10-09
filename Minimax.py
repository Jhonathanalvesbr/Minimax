import Personagem
import No
import copy

playerInimigo = []
player = []

for i in range(3):
    aux = Personagem.Personagem()
    aux.id = i
    player.append(aux)
    aux = Personagem.Personagem()
    aux.id = i
    playerInimigo.append(aux)

no = No.No()
no.altura = 0
no.player = player
no.playerInimigo = playerInimigo

def minimax(no):
    if(len(no.player) == 0):
        return
    if(len(no.playerInimigo) == 0):
        return
    if(no.altura == 4):
        return
    
    for p in no.player:
        for i in no.playerInimigo:

            novoFilho = No.No()
            novoFilho.pai = no
            e = False
            for k in no.filho:
                if(k == p):
                    e = True
                    break
            if(e == False):
                no.filho.append(novoFilho)

            if(i.vida != 0):
                i.vida -= 1
                novoFilho.playerInimigo.append(copy.deepcopy(i))
                novoFilho.player.append(copy.deepcopy(p))
                novoFilho.altura = no.altura + 1
                i.vida += 1
                minimax(novoFilho)

minimax(no)
print("Gerados: " + str(len(no.filho)))
