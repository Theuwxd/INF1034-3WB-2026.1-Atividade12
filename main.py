import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello world')
clock = pygame.time.Clock()
title_size = 60

#checagem d colisao vem antes do desenho
#COLOCAR TUDO DENTRO DO WHILE
pos_x=0
pos_y=0
collider_jogador = pygame.Rect(pos_x, pos_y, 64, 64) #posicao do jogador e tamanho do jogador #PARA O PERSONAGEM COLIDIR QUANDO ENCOSTA EM ALGUMA ESTRUTURA

old_posx= pos_x
old_posy = pos_y

#exemplo de como fazer o personagem colidir com uma caixa
if collider_jogador.colliderect(collider_caixa):
    #faz voltar para posicao anterior q ele estava 
    pos_x = old_posx
    pos_Y = old_posy


#colocar uma variavel para cada imagem q eu quero no mapa 