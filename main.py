import pygame
from pygame.locals import *
import os
import random
from Personagem import Personagem
import time
import Minimax
from No import No
import math
import AStar
import PersonagemAStar
import copy
import pygame.mixer 


class personagemDisponiveis():
    def __init__(aux, nome, caminho):
        aux.nome = nome
        aux.sprite = []
        for k in os.listdir(caminho):
            aux.sprite.append(pygame.image.load(caminho+"\\"+k))
            
def criaPlayer(sprites, inferior, superior):
    player = []
    for k in range(inferior, superior):
        aux = Personagem()
        aux.updateSprite(sprites[k].sprite, sprites[k].nome)
        player.append(aux)
    return player

def criarPersonagens():
    caminhoPersonagens = os.getcwd()+'\\castelo'
    personagem = []
    for k in os.listdir(caminhoPersonagens):
        personagem.append(personagemDisponiveis(k,caminhoPersonagens+"\\"+k))
    return personagem

sprite = criarPersonagens()
random.shuffle(sprite)
player = criaPlayer(sprite,0,3)
player[0].sprite.rect.x = 10
player[0].sprite.rect.y = 10
player[1].sprite.rect.x = 10
player[1].sprite.rect.y = player[0].sprite.rect.y+190
player[2].sprite.rect.x = 10
player[2].sprite.rect.y = player[1].sprite.rect.y+190
playerInimigo = criaPlayer(sprite,3,6)
playerInimigo[0].sprite.updateSprite
for k in playerInimigo:
    k.sprite.jogador = False
playerInimigo[0].sprite.rect.x = 480
playerInimigo[0].sprite.rect.y = 10
playerInimigo[1].sprite.rect.x = 480
playerInimigo[1].sprite.rect.y = player[0].sprite.rect.y+190
playerInimigo[2].sprite.rect.x = 480
playerInimigo[2].sprite.rect.y = player[1].sprite.rect.y+190
todas_as_sprites = pygame.sprite.Group()
velocidade = 20

for k in player:
    todas_as_sprites.add(k.sprite)

for k in playerInimigo:
    todas_as_sprites.add(k.sprite)
    
tamanhoTela = 600
pygame.init()
janela = pygame.display.set_mode((tamanhoTela,tamanhoTela))
pygame.display.set_caption('Game IA')
run = True
FPS = 60
fpsClock = pygame.time.Clock()
timeClick = 0
selecaoAtaque = []

soldado = []

def mover(personagem, movimento):
    if(personagem.fim-personagem.ini  > personagem.velocidade and movimento != None and len(movimento) > 0 ):
        if(personagem.jogador != -1):
            if(personagem.rect.x < movimento[0][0]*passo):
                personagem.angle = 0
            if(personagem.rect.x > movimento[0][0]*passo):
                personagem.angle = 180
            if(personagem.rect.y > movimento[0][1]*passo):
                personagem.angle = -90
            if(personagem.rect.y > movimento[0][1]*passo):
                personagem.angle = 90
        elif(personagem.id == -1 and personagem.seguir == True):
            if(personagem.rect.x < movimento[0][0]*passo):
                personagem.angle = 0
                personagem.image = personagem.sprites[2]
            if(personagem.rect.x > movimento[0][0]*passo):
                personagem.angle = 0
                personagem.image = personagem.sprites[1]
            if(personagem.rect.y > movimento[0][1]*passo):
                personagem.angle = 0
                personagem.image = personagem.sprites[4]
            if(personagem.rect.y > movimento[0][1]*passo):
                personagem.angle = 0
                personagem.image = personagem.sprites[3]
            
        #print(personagem.movimento)
        personagem.ini = time.time()
        personagem.rect.x = movimento[0][0]*passo
        personagem.rect.y =  movimento[0][1]*passo
        p = []
        p.append(personagem.rect.x)
        p.append(personagem.rect.y)
        movimento.pop(0)

def findXY(pernosagemAlvo):
    global caminho
    for x in range(len(caminho)):
        for y in range(len(caminho)):
            if(caminho[x][y] == pernosagemAlvo):
                return [x,y]

'''def getCaminho(personagem,pernosagemAlvo):
    movimento = []
    
    x = int(personagem.rect.x/passo)
    y = int(personagem.rect.y/passo)
    #caminho[y][x] = personagem.id

   
    xy = findXY(pernosagemAlvo)

    caminho[xy[0]][xy[1]] = pernosagemAlvo
    personagem.desX = xy[0]
    personagem.desY = xy[1]

    #imprimirCaminho()

    movimento = busca.busca(caminho,[y,x],pernosagemAlvo,x,y,personagem)

    if(movimento == None):
        return None
    #print(movimento)
    #caminho[y][x] = 0
    return movimento
'''

def getCaminho(personagem,pernosagemAlvo):
    movimento = []
    
    x = int(personagem.rect.x/passo)
    y = int(personagem.rect.y/passo)
    caminho[y][x] = personagem.id

    xy = [int((pernosagemAlvo.sprite.rect[0]+(passo*2))/passo),int((pernosagemAlvo.sprite.rect[1]+(passo*2))/passo)]
    
    caminho[xy[1]][xy[0]] = pernosagemAlvo.id
    personagem.desX = xy[1]
    personagem.desY = xy[0]

    #imprimirCaminho()

    movimento = busca.busca(caminho,[y,x],pernosagemAlvo.id,x,y,personagem)
    if(movimento == None):
        return None
    #print(movimento)
    caminho[y][x] = 0
    caminho[xy[1]][xy[0]] = 0
    return movimento


def getCaminhoSoldado(personagem,pernosagemAlvo):
    movimento = []
    
    x = int(personagem.rect.x/passo)
    y = int(personagem.rect.y/passo)
    caminho[y][x] = personagem.id

    xy = [int(pernosagemAlvo.rect.x/passo),int(pernosagemAlvo.rect.y/passo)]
    
    caminho[xy[0]][xy[1]] = pernosagemAlvo.id
    personagem.desX = xy[0]
    personagem.desY = xy[1]

    #imprimirCaminho()

    movimento = busca.busca(caminho,[y,x],pernosagemAlvo.id,x,y,personagem)

    #print(movimento)
    caminho[xy[0]][xy[1]] = 0
    caminho[y][x] = 0
    return movimento


def minimax(player, playerInimigo):
    p = []
    i = []

    for k in player:
        aux = Personagem()
        aux.ataque = k.ataque
        aux.vida = k.vida
        aux.nome = k.nome
        p.append(aux)
    for k in playerInimigo:
        aux = Personagem()
        aux.ataque = k.ataque
        aux.vida = k.vida
        aux.nome = k.nome
        i.append(aux)
    no = No(None, p, i, 0)
    Minimax.minimax(no, True, -math.inf, math.inf)
    '''for k in no.filho:
        print(k.valor)
    '''
    return no

def deletar(d):
    global player
    global playerInimigo
    global soldado
    global musicaExplosao
    global musicaAplausos
    for k in soldado:
        if(k == d):
            for i in todas_as_sprites:
                if(i == k):
                    todas_as_sprites.remove(i)
                    soldado.remove(k)
                
    for k in player:
        if(k == d):
            for i in todas_as_sprites:
                if(i == k.sprite):
                    musicaExplosao.play()
                    musicaAplausos.play()
                    todas_as_sprites.remove(i)
                    player.remove(k)
                    return
    for k in playerInimigo:
        if(k == d):
            for i in todas_as_sprites:
                if(i == k.sprite):
                    musicaExplosao.play()
                    musicaAplausos.play()
                    todas_as_sprites.remove(i)
                    playerInimigo.remove(k)
                    return

#d = player[0]
#deletar(d)
#d = player[0]
#deletar(d)
player[1].ataque = 3
player[0].vida = 10
playerInimigo[0].vida = 10
playerInimigo[1].ataque = 3

y = 10
x = 0
for k in player:
    k.id = y
    y += 1
    k.sprite.vidaTotal = k.vida
    k.sprite.velocidadeTotal = k.level*(velocidade/2)
    k.velocidade = x
    x += 1
x = 0
y = -10
for k in playerInimigo:
    k.id = y
    y -= 1
    k.sprite.vidaTotal = k.vida
    k.sprite.velocidadeTotal = k.level*velocidade
    k.velocidade = x
    x += 1

texturaGrama = pygame.image.load(os.getcwd()+"\\pacote\\textura\\grama4.jpg")
texturaGrama = pygame.transform.scale(texturaGrama,(int(600),int(600)))
posicaoTexturaGrama = texturaGrama.get_rect(midleft=(0, +300))
timeVelocidade = time.time()
passo = 25
tamanho = int(600/passo)
busca = AStar.Astar(tamanho)
caminho = []
for y in range(tamanho):
    linha = []
    for x in range(tamanho):
        linha.append(0)
    caminho.append(linha)

#soldadoSprite = [pygame.image.load(os.getcwd()+"\\pacote\\soldado\\1.png")]
#soldado = PersonagemAStar.Personagem()
#soldado.sprite(soldadoSprite)
#soldado.personagem = player[0]
#soldado.id = 30
#todas_as_sprites.add(soldado)
'''
for k in caminho:
    for i in player:
        y = int(i.sprite.rect.y/passo)
        x = int(i.sprite.rect.x/passo)
        for j in range(y,y+4):
            for z in range(x,x+4):
                caminho[j+2][z+1] = i.id
    for i in playerInimigo:
        y = int(i.sprite.rect.y/passo)
        x = int(i.sprite.rect.x/passo)
        for j in range(y,y+4):
            for z in range(x,x+4):
                caminho[j+3][z+1] = i.id
'''

def batalha():
    global musicaBatalha
    e = False
    for k in range(0,5):
        if(pygame.mixer.Channel(k).get_sound() == musicaBatalha):
            e = True
            break
    if(e == False):
        musicaBatalha.play()
    return

def encosta(personagem):
    global player
    global playerInimigo
    global timeRun

    if(timeRun-personagem.fim < 1):
        return None
    else:
        personagem.fim = time.time()

    p = []
    p.append(personagem.rect.x)
    p.append(personagem.rect.y)
    for k in player:
        if(k.sprite.rect.collidepoint(p)):
            k.vida -= personagem.ataque
            batalha()
            return None
    for k in playerInimigo:
        if(k.sprite.rect.collidepoint(p)):
            batalha()
            k.vida -= personagem.ataque
            return None


def imprimirCaminho():
    global caminho
    for x in range(len(caminho)):
        for y in range(len(caminho)):
            print(caminho[x][y], end="")
        print()

def verificaVida():
    global player
    global playerInimigo
    
    for k in player:
        if(k.vida <= 0):
            deletar(k)
    for k in playerInimigo:
        if(k.vida <= 0):
            deletar(k)
    for k in soldado:
        if(k.vida <= 0):
            deletar(k)

def procuraSoldado():
    global soldado
    
    for k in soldado:
        e = False
        for s in soldado:
            if(k != s and k.jogador != s.jogador):
                if(abs(k.x - s.x) <= 3 and abs(k.y - s.y) <= 3 and
                abs(k.x - s.x) >= -3 and abs(k.y - s.y) >= -3 and k.caminhar == False):
                    batalha()
                    e = True
                    k.caminhar = True
                    k.movimento = getCaminhoSoldado(k,s)
                if(k.rect.colliderect(s.rect)):
                    global musicaHit
                    e = True
                    r = random.randrange(0,15)
                    if(r == 5):
                        musicaHit.play()
                    k.caminhar = True
                    k.vida -= s.ataque
                    s.vida -= k.ataque
                if(k.rect.colliderect(s.rect) and abs(k.x - s.x) <= 1 and abs(k.y - s.y) <= 1 and
                abs(k.x - s.x) >= -1 and abs(k.y - s.y) >= -1):
                    k.movimento = None
                    e = True

     
        if(e == False and k.movimento == None):
            k.movimento = getCaminho(k,k.find[0])
            k.caminhar = False

                   

#deletar(playerInimigo[1])
#deletar(playerInimigo[1])
timeRun = 0

musicaTema = pygame.mixer.music.load(os.getcwd()+"\\pacote\\mp3\\tema.mp3")
musicaSelecaoPlayer = pygame.mixer.Sound(os.getcwd()+"\\pacote\\mp3\\player.mp3")
musicaSelecaoInimigo = pygame.mixer.Sound(os.getcwd()+"\\pacote\\mp3\\inimigo.mp3")
musicaBatalha = pygame.mixer.Sound(os.getcwd()+"\\pacote\\mp3\\luta.mp3")
musicaExplosao = pygame.mixer.Sound(os.getcwd()+"\\pacote\\mp3\\explosao.mp3")
musicaAplausos = pygame.mixer.Sound(os.getcwd()+"\\pacote\\mp3\\aplausos.mp3")
musicaHit = pygame.mixer.Sound(os.getcwd()+"\\pacote\\mp3\\hit.mp3")
musicaHit.set_volume(0.5)
pygame.mixer.music.play(-1)

def procuraNovoCastelo(soldado):
    global player
    global playerInimigo
    e = False
    if(soldado.jogador == True):
        for k in playerInimigo:
            if(soldado.find[0] == k):
                e = True
    elif(soldado.jogador == False):
        for k in player:
            if(soldado.find[0] == k):
                e = True
    if(e == True):
        return getCaminho(soldado,soldado.find[0])

    if(e == False and soldado.jogador == True):
        if(len(playerInimigo) == 0):
            return
        r = random.randint(0,len(playerInimigo)-1)
        soldado.find[0] = playerInimigo[r]
    if(e == False and soldado.jogador == False):
        if(len(player) == 0):
            return
        r = random.randint(0,len(player)-1)
        soldado.find[0] = player[r]
    
    return getCaminho(soldado,soldado.find[0])


while run:
    janela.blit(texturaGrama,posicaoTexturaGrama)

    for event in pygame.event.get():
        teclado = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            run = False
       # if(teclado[pygame.K_F5]):
        #    mov = getCaminho(soldado,-12)
        #    soldado.ini = time.time()
        #    soldado.movimento = mov
    
    
    
    
    
    #soldado.fim = time.time()
    #if(len(soldado.movimento) > 1):
    #    mover(soldado,soldado.movimento)
    #if(len(soldado.movimento) <= 1):
    #    encosta(soldado,playerInimigo)
    
    
    timeRun = time.time()

    if(timeRun-timeVelocidade > 1):
        procuraSoldado()
        for j in playerInimigo:
            if(j.velocidade <= 0):
                j.velocidade  = j.level*velocidade
                auxSoldadoSprite = [pygame.image.load(os.getcwd()+"\\pacote\\soldado\\3.png")] 
                aux = PersonagemAStar.Personagem()
                aux.sprite(auxSoldadoSprite)
                aux.personagem = j
                aux.id = j.id*3
                aux.jogador = j.sprite.jogador
                aux.ataque = j.ataque/10
                aux.vida = j.vida
                aux.fim = time.time()
                aux.vidaTotal = j.vida
                aux.rect = copy.deepcopy(j.sprite.rect)
                aux.rect.x = ((j.sprite.rect.x/passo)-1)*passo
                aux.rect.y = ((j.sprite.rect.y/passo)-1)*passo

                aux.spriteVida = pygame.image.load(os.getcwd()+"\\pacote\\barra\\Loading Bar Background.png")
                aux.spriteVida = pygame.transform.scale(aux.spriteVida,(int(80),int(20)))
                aux.posicaoVida = aux.spriteVida.get_rect(midleft=(80, 20))

                aux.spriteCaregarVida = pygame.image.load(os.getcwd()+"\\pacote\\barra\\Loading Bar Green.png")
                aux.spriteCaregarVida = pygame.transform.scale(aux.spriteCaregarVida,(int(78),int(20)))
                aux.posicaoCarregar = aux.spriteCaregarVida.get_rect(midleft=(80, 20))

                aux.spriteRed = pygame.image.load(os.getcwd()+"\\pacote\\barra\\Barra_Vermelho.png")
                aux.spriteRed = pygame.transform.scale(aux.spriteRed,(int(78),int(20)))
                aux.posicaoRed = aux.spriteRed.get_rect(midleft=(80, 20))
                aux.spriteVida = pygame.transform.smoothscale( aux.spriteVida, (int(25), int(5)) )
                aux.spriteRed = pygame.transform.smoothscale( aux.spriteRed, (int(25), int(5)) )
                aux.spriteCaregarVida = pygame.transform.smoothscale( aux.spriteCaregarVida, (int(25), int(5)))
                soldado.append(aux)
                j.personagemAStar.append(aux)
                no = minimax(player, playerInimigo)
                joagada = None
                valor = -math.inf
                for k in no.filho:
                    if(valor < k.valor):
                        valor = k.valor
                        jogada = k
                '''
                nome = jogada.id[1].nome
                mov = []
                for k in player:
                    if(k.nome == nome):
                        aux.find.append(k.id)
                        mov = getCaminho(aux,aux.find[0])
                        exit()
                        break
                '''
                nome = jogada.id[1].nome
                mov = []
                for k in player:
                    if(k.nome == nome):
                        aux.find.append(k)
                        mov = getCaminho(aux,k)
                        break
                
                aux.ini = time.time()
                aux.movimento = mov
                todas_as_sprites.add(aux)
            else:
                j.velocidade -= 1
        for j in player:
            if(j.velocidade > 0):
                j.velocidade -= 1
        timeVelocidade = time.time()
    
        
    if(pygame.mouse.get_pressed()[0] == True):
        ponto = pygame.mouse.get_pos()
        if(timeRun-timeClick > 0.1):
            #print(str(ponto[0]/passo) + " : " + str(ponto[1]/passo))
            for p in player:
                if(p.sprite.rect.collidepoint(ponto)):
                    if(len(selecaoAtaque) == 0):
                        musicaSelecaoPlayer.play()
                        selecaoAtaque.append(p)
                    else:
                        for k in player:
                            if(k == selecaoAtaque[0]):
                                selecaoAtaque[0] = p
                                break
            for p in playerInimigo:
                if(p.sprite.rect.collidepoint(ponto)):
                    if(len(selecaoAtaque) == 1):
                        musicaSelecaoInimigo.play()
                        selecaoAtaque.append(p)
                    elif(len(selecaoAtaque) > 1):
                        for k in playerInimigo:
                            if(k == selecaoAtaque[1]):
                                selecaoAtaque[1] = p
                                break

    if(len(selecaoAtaque) >= 2):
        if(selecaoAtaque[0].velocidade == 0):

                auxSoldadoSprite = [pygame.image.load(os.getcwd()+"\\pacote\\soldado\\4.png")] 
                aux = PersonagemAStar.Personagem()
                aux.sprite(auxSoldadoSprite)
                aux.personagem = j
                aux.id = selecaoAtaque[0].id*3
                aux.jogador = selecaoAtaque[0].sprite.jogador
                aux.ataque = selecaoAtaque[0].ataque/10
                aux.vida = selecaoAtaque[0].vida
                aux.fim = time.time()
                aux.vidaTotal = selecaoAtaque[0].vida
                aux.rect = copy.deepcopy(selecaoAtaque[0].sprite.rect)
                aux.rect.x = ((selecaoAtaque[0].sprite.rect.x/passo)+4)*passo
                aux.rect.y = ((selecaoAtaque[0].sprite.rect.y/passo)+3)*passo

                aux.spriteVida = pygame.image.load(os.getcwd()+"\\pacote\\barra\\Loading Bar Background.png")
                aux.spriteVida = pygame.transform.scale(aux.spriteVida,(int(80),int(20)))
                aux.posicaoVida = aux.spriteVida.get_rect(midleft=(80, 20))

                aux.spriteCaregarVida = pygame.image.load(os.getcwd()+"\\pacote\\barra\\Loading Bar Green.png")
                aux.spriteCaregarVida = pygame.transform.scale(aux.spriteCaregarVida,(int(78),int(20)))
                aux.posicaoCarregar = aux.spriteCaregarVida.get_rect(midleft=(80, 20))

                aux.spriteRed = pygame.image.load(os.getcwd()+"\\pacote\\barra\\Barra_Vermelho.png")
                aux.spriteRed = pygame.transform.scale(aux.spriteRed,(int(78),int(20)))
                aux.posicaoRed = aux.spriteRed.get_rect(midleft=(80, 20))
                aux.spriteVida = pygame.transform.smoothscale( aux.spriteVida, (int(25), int(5)) )
                aux.spriteRed = pygame.transform.smoothscale( aux.spriteRed, (int(25), int(5)) )
                aux.spriteCaregarVida = pygame.transform.smoothscale( aux.spriteCaregarVida, (int(25), int(5)))
                soldado.append(aux)
                selecaoAtaque[0].personagemAStar.append(aux)
                '''
                nome = selecaoAtaque[1].nome
                mov = []
                for k in playerInimigo:
                    if(k.nome == nome):
                        aux.find.append(k.id)
                        mov = getCaminho(aux,aux.find[0])
                        break
                '''
                nome = selecaoAtaque[1].nome
                mov = []
                for k in playerInimigo:
                    if(k.nome == nome):
                        aux.find.append(k)
                        mov = getCaminho(aux,k)
                        break
                
                aux.ini = time.time()
                aux.movimento = mov
                
                todas_as_sprites.add(aux)




                
                selecaoAtaque[0].velocidade = k.level*(velocidade/2)
                print(selecaoAtaque[0].nome + " -> " + selecaoAtaque[1].nome)
                selecaoAtaque = []
   
    
                
                '''

                for k in player:
                    print(k.nome)
                
                selecaoAtaque = []
                x = 0
                play = []
                for k in playerInimigo:
                    if(k.velocidade <= 0):
                        k.velocidade  = len(playerInimigo)-1
                        play.append(k)
                    else:
                        k.velocidade -= 1
                    print("Velocidade: " + str(k.velocidade))
                
                no = minimax(player, playerInimigo)
            
                joagada = None
                valor = -math.inf
                for k in no.filho:
                    if(valor < k.valor):
                        valor = k.valor
                        jogada = k
                for p in player:
                    if(p.nome == jogada.id[1].nome):
                        p.vida -= jogada.id[0].ataque
                        break
                        
                
                print(jogada.id[1].nome + " <- " + jogada.id[0].nome)

                for k in player:
                    if(k.vida <= 0):
                        deletar(k)
                

                
                

        timeClick = time.time()

        '''

    for k in soldado:
        k.x = k.rect.x/passo
        k.y = k.rect.x/passo
        if((k.movimento) != []):
            mover(k,k.movimento)

        encosta(k)
        if(k.movimento == []):
            k.movimento = procuraNovoCastelo(k)

    verificaVida()
    
    todas_as_sprites.draw(janela)
    todas_as_sprites.update(janela)
    '''
    pygame.draw.line(janela, pygame.Color(255,255,255), (0, 700), (800, 700), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (0, 600), (800, 600), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (0, 500), (800, 500), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (0, 400), (800, 400), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (0, 300), (800, 300), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (0, 200), (800, 200), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (0, 100), (800, 100), 1)


    pygame.draw.line(janela, pygame.Color(255,255,255), (100, 0), (100, 800), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (200, 0), (200, 800), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (300, 0), (300, 800), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (400, 0), (400, 800), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (500, 0), (500, 800), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (600, 0), (600, 800), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (700, 0), (700, 800), 1)
    '''
    pygame.display.update()
    janela.fill((0,0,0))
    fpsClock.tick(FPS)

pygame.quit()
