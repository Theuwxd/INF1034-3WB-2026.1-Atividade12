import pygame
import sys
from pygame.locals import QUIT, KEYDOWN


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello world')
clock = pygame.time.Clock()



hero_sprite = pygame.image.load('personagem.png')

direcoes = {
    'baixo': 0,
    'dir':   1,
    'esq':   2,
    'cima':  3,
}
direcao = 'baixo'
curr_frame = 0
anim_time = 0
pos_x = 400
pos_y = 300
velocidade = 2
movendo = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()

    keys = pygame.key.get_pressed()
    movendo = False

    if keys[pygame.K_RIGHT]:
        pos_x += velocidade
        direcao = 'dir'
        movendo = True
    elif keys[pygame.K_LEFT]:
        pos_x -= velocidade
        direcao = 'esq'
        movendo = True
    elif keys[pygame.K_UP]:
        pos_y -= velocidade
        direcao = 'cima'
        movendo = True
    elif keys[pygame.K_DOWN]:
        pos_y += velocidade
        direcao = 'baixo'
        movendo = True

    if movendo:
        anim_time += dt
        if anim_time / 1000 > 0.15:
            curr_frame = curr_frame + 1
            if curr_frame > 3:
                curr_frame = 0
            anim_time = 0

    else:
        curr_frame = 0

    screen.fill((255, 255, 255))

    #pra calcular o tamanho de cada frame
    #sem isso tava ficando tudo cortado, pq as imagens n batiam na msm largura e altura
    img = direcoes[direcao]
    #retornar o tamanho da imagem
    larg, alt = hero_sprite.get_size()
    frame_larg = larg // 4
    frame_alt  = alt // 4
    #diminuir o tamanho so pra ficar mais bonitinho na imagem
    frame_rect = (curr_frame * frame_larg, img * frame_alt, frame_larg, frame_alt)
    #vou recortar o frame
    frame = hero_sprite.subsurface(frame_rect)
    #vou alterar para o tamanho q eu quero
    frame = pygame.transform.scale(frame, (32, 48))
    screen.blit(frame, (pos_x, pos_y))

    pygame.display.update()
