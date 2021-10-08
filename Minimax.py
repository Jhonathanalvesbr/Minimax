import copy
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
        
        return 
    if(len(no.playerInimigo) == 0):
        
        return 
    if(no.altura == 4):
        return 
    
    if(jogada):
        x = 0
        for p in no.player:
            y = 0
            for i in no.playerInimigo:
                if(i.vida == 0):
                    no.playerInimigo.remove(i)
                    y -= 1
                else:
                    filho = No(copy.deepcopy(no.player), copy.deepcopy(no.playerInimigo), x, y)
                    filho.pai = no
                    no.filho.append(filho)
                    
                    filho.altura = no.altura + 1
                    filho.playerInimigo[0].vida -= 1
                    

                    minimax(filho,True)
                                        
                    y += 1
            x += 1
            
         
    
    
    

no = No(player, playerInimigo, None, None)
no.altura = 0

print(minimax(no, True))
