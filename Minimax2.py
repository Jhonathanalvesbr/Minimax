import Personagem
import No
import copy

playerInimigo = []
player = []

for i in range(3):
    aux = Personagem.Personagem()
    player.append(aux)
    aux = Personagem.Personagem()
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
    
    i = 0
    while(i < len(no.player)):
        j = 0
        while(j < len(no.playerInimigo)):
            if(no.playerInimigo[j].vida == 0):
                no.playerInimigo.pop(j)
                j -= 1
            else:
                novoFilho = No.No()
                novoFilho.pai.insert(0,no)
                no.filho.insert(0,novoFilho)
                
                for k in no.player:
                    aux = Personagem.Personagem()
                    aux.ataque = k.ataque * 1
                    aux.level = k.level * 1
                    aux.vida = k.vida * 1
                    novoFilho.player.append(aux)

                for k in no.playerInimigo:
                    aux = Personagem.Personagem()
                    aux.ataque = k.ataque * 1
                    aux.level = k.level * 1
                    aux.vida = k.vida * 1
                    novoFilho.playerInimigo.append(aux)

                novoFilho.altura = (no.altura + 1) * 1
                novoFilho.playerInimigo[j].vida -= no.player[i].ataque

                minimax(novoFilho)

            j += 1

        i += 1

minimax(no)
print(len(no.filho))
