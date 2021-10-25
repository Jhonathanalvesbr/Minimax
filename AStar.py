import math
import Estado
import random
from scipy.spatial.distance import cdist
from scipy.spatial import distance
from bisect import insort

qntPassos = 0

def inserir(lista, aux):

    j = 0
    while(len(lista) > 0 and j < len(lista) and aux.f > lista[j].f):
        #print(lista[j].f)
        j += 1
    #print("============")
    lista.insert(j, aux)
    
    return lista

def existe(lista, filho):
    if(len(lista) == 0):
        return -1
    for i in lista:
        if(i.x == filho.x and i.y == filho.y):
            return 1
    return -1

def custoH(x, y, desX, desY):
    dx = abs (x-desX)
    dy = abs (y-desX)
    a = [x,y]
    b = [desX, desY]


    f = abs(x-desX) + abs(y-desY)
    h = abs(x-desX) + abs(y-desY)
    
    #print("Caminho[" + str(x) + "]["+ str(y) + "] -- F(n): " + str(f+g) + " -- G(n): " + str(g) + " -- H(n): " + str(h))
    #return g
    #return distance.euclidean(a, b)+g
    #return g * (dx * dx + dy * dy)
    #return sum(abs(val1-val2)-g for val1, val2 in zip(a,b)) #manhattan
    #return abs(max(dx,dy)) #A quantidade de nós gerados foram: 58  - Custo total: 18
    #A quantidade de nós gerados foram: 125 - Custo total: 18
    #return (dx*dy) + (dy*dy)  #A quantidade de nós gerados foram: 170 - Custo total: 32
    #return math.sqrt(dx*dx + dy*dy)  # A quantidade de nós gerados foram: 102 - Custo total: 23
    #return (dx + dy)  #A quantidade de nós gerados foram: 270 - Custo total: 19
    #return abs(dx) + abs(dy) #A quantidade de nós gerados foram: 94 - Custo total: 23
    #return abs(x - desX) + abs(y - desY)  #A quantidade de nós gerados foram: 94 - Custo total: 23
    #return math.sqrt(pow((x - desX), 2.0)+pow((y - desY), 2.0))  #A quantidade de nós gerados foram: 102 - Custo total: 23
    #return abs(dx)+abs(dy)

    #return -1
    #return abs(min(dx,dy))
    #return g #Profundidade
    return abs(x-desX) + abs(y-desY) #Manhattan
    #return math.sqrt(pow((x - desX), 2.0)+pow((y - desY), 2.0)) #Euclidiana
    #return 0

def criaEstado(self, iniX, iniY):
    # Baixo
    if(iniX+1 >= 0 and iniY >= 0 and iniX+1 < self.tamanho and iniY < self.tamanho and self.caminho[iniX+1][iniY] == 0):
        # print("Baixo")
        return Estado.Estado(iniX+1, iniY)
        # Cima
    elif(iniX-1 >= 0 and iniY >= 0 and iniX-1 < self.tamanho and iniY < self.tamanho and self.caminho[iniX-1][iniY] == 0):
        # print("Cima")
        return Estado.Estado(iniX-1, iniY)
        # Direita
    elif(iniX >= 0 and iniY+1 >= 0 and iniX < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX][iniY+1] == 0):
        # print("Direita")
        return Estado.Estado(iniX, iniY+1)
        # Esquerda
    elif(iniX >= 0 and iniY-1 >= 0 and iniX < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX][iniY-1] == 0):
        # print("Esquerda")
        return Estado.Estado(iniX, iniY-1)
        # 135
    else:
        return -1
    '''
    elif(iniX+1 >= 0 and iniY+1 >= 0 and iniX+1 < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX+1][iniY+1] == 0):
        # print("135")
        return Estado.Estado(iniX+1, iniY+1)
        # 225
    elif(iniX+1 >= 0 and iniY-1 >= 0 and iniX+1 < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX+1][iniY-1] == 0):
        # print("225")
        return Estado.Estado(iniX+1, iniY-1)
        # 315
    elif(iniX-1 >= 0 and iniY-1 >= 0 and iniX-1 < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX-1][iniY-1] == 0):
        # print("315")
        return Estado.Estado(iniX-1, iniY-1)
        # 45
    elif(iniX-1 >= 0 and iniY+1 >= 0 and iniX-1 < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX-1][iniY+1] == 0):
        # print("45")
        return Estado.Estado(iniX-1, iniY+1)
    else:
        return -1
    '''

def getCaminho(filho):
    pai = filho.parente
    lista = []
    lista.append([filho.y, filho.x])
    while(pai.parente != []):
        lista.append([pai.y, pai.x])
        pai = pai.parente
    return list(reversed(lista))

class Astar():
    caminho = []
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def criarNo(self, q, i):
        if(q == -1):
            return
        iniX = q.x
        iniY = q.y
        # Baixo
        if(iniX+1 >= 0 and iniY >= 0 and iniX+1 < self.tamanho and iniY < self.tamanho and self.caminho[iniX+1][iniY] == 0 and i == 0):
            # print("Baixo")
            return (Estado.Estado(iniX+1, iniY))
        # Cima
        elif(iniX-1 >= 0 and iniY >= 0 and iniX-1 < self.tamanho and iniY < self.tamanho and self.caminho[iniX-1][iniY] == 0 and i == 1):
            # print("Cima")
            return (Estado.Estado(iniX-1, iniY))
        # Direita
        elif(iniX >= 0 and iniY+1 >= 0 and iniX < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX][iniY+1] == 0 and i == 2):
            # print("Direita")
            return (Estado.Estado(iniX, iniY+1))
        # Esquerda
        elif(iniX >= 0 and iniY-1 >= 0 and iniX < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX][iniY-1] == 0 and i == 3):
            # print("Esquerda")
            return (Estado.Estado(iniX, iniY-1))
        # 135
        '''
        elif(iniX+1 >= 0 and iniY+1 >= 0 and iniX+1 < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX+1][iniY+1] == 0 and i == 4):
            # print("135")
            return (Estado.Estado(iniX+1, iniY+1))
        # 225
        elif(iniX+1 >= 0 and iniY-1 >= 0 and iniX+1 < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX+1][iniY-1] == 0 and i == 5):
            # print("225")
            return (Estado.Estado(iniX+1, iniY-1))
        # 315
        elif(iniX-1 >= 0 and iniY-1 >= 0 and iniX-1 < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX-1][iniY-1] == 0 and i == 6):
            # print("315")
            return (Estado.Estado(iniX-1, iniY-1))
        # 45
        elif(iniX-1 >= 0 and iniY+1 >= 0 and iniX-1 < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX-1][iniY+1] == 0 and i == 7):
            # print("45")
            return (Estado.Estado(iniX-1, iniY+1))
        '''

    def win(self, e, target):
        if(e == -1):
            return -1
        iniX = e.x
        iniY = e.y
        # Baixo
        if(iniX+1 >= 0 and iniY >= 0 and iniX+1 < self.tamanho and iniY < self.tamanho and self.caminho[iniX+1][iniY] == target):
            # print("Baixo")
            return Estado.Estado(iniX+1, iniY)
        # Cima
        elif(iniX-1 >= 0 and iniY >= 0 and iniX-1 < self.tamanho and iniY < self.tamanho and self.caminho[iniX-1][iniY] == target):
            # print("Cima")
            return Estado.Estado(iniX-1, iniY)
        # Direita
        elif(iniX >= 0 and iniY+1 >= 0 and iniX < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX][iniY+1] == target):
            # print("Direita")
            return Estado.Estado(iniX, iniY+1)
        # Esquerda
        elif(iniX >= 0 and iniY-1 >= 0 and iniX < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX][iniY-1] == target):
            # print("Esquerda")
            return Estado.Estado(iniX, iniY-1)
        # 135
        '''
        elif(iniX+1 >= 0 and iniY+1 >= 0 and iniX+1 < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX+1][iniY+1] == target):
            # print("135")
            return Estado.Estado(iniX+1, iniY+1)
        # 225
        elif(iniX+1 >= 0 and iniY-1 >= 0 and iniX+1 < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX+1][iniY-1] == target):
            # print("225")
            return Estado.Estado(iniX+1, iniY-1)
        # 315
        elif(iniX-1 >= 0 and iniY-1 >= 0 and iniX-1 < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX-1][iniY-1] == target):
            # print("315")
            return Estado.Estado(iniX-1, iniY-1)
        # 45
        elif(iniX-1 >= 0 and iniY+1 >= 0 and iniX-1 < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX-1][iniY+1] == target):
            # print("45")
            return Estado.Estado(iniX-1, iniY+1)
        else:
            return -1
            '''

    def imprimir(self, caminho):
        self.caminho = self.caminho
        for x in range(len(self.caminho)):
            for y in range(len(self.caminho)):
                print(self.caminho[x][y], end="")
                print("|", end="")
            print()
        print()
        
    def buscaIndices(self,indice,tamanho):
        indice1 = indice
        indice2 = indice
        t = tamanho
        if(t > self.tamanho):
            t = self.tamanho
        while(t > 0):
            if(indice1 > 0):
                t -= 1
                indice1 -= 1
                if(t == 0):
                    break
            if(indice2 < self.tamanho):
                indice2 += 1
                t -= 1
        
        return [indice1,indice2]

    def busca(self, c, posicaoPersonagemXY, target, posicaoX, posicaoY, personagem):
        global qntPassos
        caminho = c[:]
        iniX = posicaoPersonagemXY[0]
        iniY = posicaoPersonagemXY[1]
        if(iniX == personagem.desX and iniY == personagem.desY):
            personagem.desX = None
        xx = self.buscaIndices(posicaoX,personagem.tamanho)
        yy = self.buscaIndices(posicaoY,personagem.tamanho)
    
        e = 0

        for x in range(xx[0],xx[1]):
            for y in range(yy[0],yy[1]):
                #print(caminho[x][y], end="")
                if(caminho[x][y] == target):
                    personagem.desX = x
                    personagem.desY = y
                    e = 1
                    personagem.find = 1
                    break


            #print("")
        
        if(e == 0 and personagem.caminhar == True and personagem.desX == None):
            personagem.find = -1
            xTemp = random.randint(xx[0],xx[1])
            yTemp = random.randint(yy[0],yy[1])
            if(xTemp == self.tamanho):
                xTemp -= 1
            if(yTemp == self.tamanho):
                yTemp -= 1

            personagem.desX = xTemp
            personagem.desY = yTemp

        if(personagem.caminhar == True):
            caminho[personagem.desX][personagem.desY] = -2
            target  = -2


        #print(personagem.desX)
        #print(personagem.desY)
        #print("============")
        if(personagem.desX == None):
            return None
        
        listaAberta = []
        listaFechada = []
        self.caminho = caminho
        listaAberta.append(Estado.Estado(iniX, iniY))

        while(len(listaAberta) > 0):
            pai = listaAberta[0]
            listaFechada.append(pai)
            listaAberta.pop(0)
            w = self.win(pai,target)
            if(w != None):
                #for i in listaAberta:
                #    print(i.f)
                #print("Win")
                w.parente = pai
                getCamin = getCaminho(w)
                qntPassos += 1
                if(personagem.id == 1):
                    #custoH(w.x, w.y, personagem.desX, personagem.desY, filho.g)
                    #print("Caminho[" + str(w.x) + "]["+ str(w.y) + "] -- F(n): " + str(w.f) + " -- G(n): " + str(w.g) + " -- H(n): " + str(w.h))
                    print("A quantidade de nós gerados foram: " + str(qntPassos))
                    print("Custo total: " + str(len(getCamin)))
                qntPassos = 0

                return getCamin
            for i in range(8):
                filho = self.criarNo(pai, i)
                if(filho != None and existe(listaAberta, filho) != 1 and existe(listaFechada, filho) != 1):
                    qntPassos += 1
                    filho.g = pai.g + 1.0
                    filho.h = custoH(filho.x, filho.y, personagem.desX, personagem.desY)
                    filho.f = filho.h+filho.g
                    #print(filho.f)
                    filho.parente = pai
                    inserir(listaAberta, filho)
        print("Não achou!")

    def imprimirCaminho(self, e):
        a = e.parente
        while(a.parente != []):
            for x in range(self.tamanho):
                for y in range(self.tamanho):
                    if(a.x == x and a.y == y):
                        print("2", end="")
                    else:
                        print("0", end="")
                print()
            print()
            a = a.parente

    def CaminhoVazio(self, caminho, target):
        for x in range(len(self.caminho)):
            for y in range(len(self.caminho)):
                if(self.caminho[x][y] == target):
                    return 1
        return -1
