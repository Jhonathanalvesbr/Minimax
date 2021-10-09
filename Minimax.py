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

k = 0

def minimax(no):
    global k
    if(len(no.player) == 0):
        return
    if(len(no.playerInimigo) == 0):
        return
    if(no.altura == 4):
        return
    
    p = 0
    while p < len(no.player):
        i = 0
        while i < len(no.playerInimigo):
            if(no.playerInimigo[i].vida != 0):
                novoFilho = No.No()
                novoFilho.pai = no
                no.filho.append(novoFilho)
                
                for x in no.player:
                    aux = Personagem.Personagem()
                    aux.ataque = x.ataque
                    aux.vida = x.vida
                    aux.level = x.level
                    aux.id = x.id
                    novoFilho.player.append(aux)

                for x in no.playerInimigo:
                    aux = Personagem.Personagem()
                    aux.ataque = x.ataque
                    aux.vida = x.vida
                    aux.level = x.level
                    aux.id = x.id
                    novoFilho.playerInimigo.append(aux)
                
                #print(k)
                k += 1

                    
                novoFilho.altura = no.altura + 1

                    
                minimax(novoFilho)
            i += 1
        p += 1

minimax(no)
print("Gerados: " + str(len(no.filho)))
