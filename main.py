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

class personagemDisponiveis():
    def __init__(self, nome, caminho):
        self.nome = nome
        self.sprite = []
        for k in os.listdir(caminho):
            self.sprite.append(pygame.image.load(caminho+"\\"+k))
            
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

def getCaminho(personagem,pernosagemAtual,pernosagemAlvo):
    movimento = []
    
    x = int(personagem.rect.x/passo)
    y = int(personagem.rect.y/passo)
    caminho[y][x] = pernosagemAtual
    movimento = busca.busca(caminho,[y,x],pernosagemAlvo,x,y,personagem)
    if(movimento == None):
        return None
    #print(movimento)
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
    for k in no.filho:
        print(k.valor)
    return no

def deletar(d):
    global player
    global playerInimigo
    for k in player:
        if(k == d):
            for i in todas_as_sprites:
                if(i == k.sprite):
                    todas_as_sprites.remove(i)
                    player.remove(k)
                    break
            return
    for k in playerInimigo:
        if(k == d):
            for i in todas_as_sprites:
                if(i == k.sprite):
                    todas_as_sprites.remove(i)
                    playerInimigo.remove(k)
                    break
            return

#d = player[0]
#deletar(d)
#d = player[0]
#deletar(d)
player[1].ataque = 3
playerInimigo[1].ataque = 3

y = 2
x = 0
for k in player:
    k.id = y
    y += 1
    k.sprite.vidaTotal = k.vida
    k.sprite.velocidadeTotal = 10
    k.velocidade = x
    x += 1
x = 0
y = -2
for k in playerInimigo:
    k.id = y
    y -= 1
    k.sprite.vidaTotal = k.vida
    k.sprite.velocidadeTotal = 10
    k.velocidade = x
    x += 1

texturaGrama = pygame.image.load(os.getcwd()+"\\pacote\\textura\\grama.jpg")
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

soldadoSprite = [pygame.image.load(os.getcwd()+"\\pacote\\soldado\\1.png")]
soldado = PersonagemAStar.Personagem()
soldado.sprite(soldadoSprite)
soldado.id = 2
todas_as_sprites.add(soldado)

for k in caminho:
    for i in player:
        y = int(i.sprite.rect.y/passo)
        x = int(i.sprite.rect.x/passo)
        for j in range(y,y+5):
            for z in range(x,x+5):
                caminho[j][z] = i.id
    for i in playerInimigo:
        y = int(i.sprite.rect.y/passo)
        x = int(i.sprite.rect.x/passo)
        for j in range(y,y+5):
            for z in range(x,x+5):
                caminho[j][z] = i.id


for x in range(len(caminho)):
    for y in range(len(caminho)):
        print(caminho[x][y], end="")
    print()


while run:
    janela.blit(texturaGrama,posicaoTexturaGrama)

    for event in pygame.event.get():
        teclado = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            run = False
        if(teclado[pygame.K_F5]):
            temp = getCaminho(soldado,1,-3)

    timeRun = time.time()

    if(timeRun-timeVelocidade > 1):
        for j in playerInimigo:
            if(j.velocidade <= 0):
                j.velocidade  = 10
            else:
                j.velocidade -= 1
        for j in player:
            if(j.velocidade <= 0):
                j.velocidade = 10
            else:
                j.velocidade -= 1
        timeVelocidade = time.time()

    if(pygame.mouse.get_pressed()[0] == True):
        ponto = pygame.mouse.get_pos()
        if(timeRun-timeClick > 0.5):
            print(str(ponto[0]/passo) + " : " + str(ponto[1]/passo))
            for p in player:
                if(p.sprite.rect.collidepoint(ponto)):
                    if(len(selecaoAtaque) == 0):
                        selecaoAtaque.append(p)
                    else:
                        for k in player:
                            if(k == selecaoAtaque[0]):
                                selecaoAtaque[0] = p
                                break
            for p in playerInimigo:
                if(p.sprite.rect.collidepoint(ponto)):
                    if(len(selecaoAtaque) == 1):
                        selecaoAtaque.append(p)
                    elif(len(selecaoAtaque) > 1):
                        for k in playerInimigo:
                            if(k == selecaoAtaque[1]):
                                selecaoAtaque[1] = p
                                break
            if(len(selecaoAtaque) >= 2):
                selecaoAtaque[1].vida -= selecaoAtaque[0].ataque
                print(selecaoAtaque[0].nome + " -> " + selecaoAtaque[1].nome)
                for k in playerInimigo:
                    if(k.vida <= 0):
                        deletar(k)
                

                for k in player:
                    print(k.nome)
                
                selecaoAtaque = []
                x = 0
                '''play = []
                for k in playerInimigo:
                    if(k.velocidade <= 0):
                        k.velocidade  = len(playerInimigo)-1
                        play.append(k)
                    else:
                        k.velocidade -= 1
                    print("Velocidade: " + str(k.velocidade))
                '''
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



    
    todas_as_sprites.draw(janela)
    todas_as_sprites.update(janela)
    
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
    
    pygame.display.update()
    janela.fill((0,0,0))
    fpsClock.tick(FPS)

pygame.quit()
