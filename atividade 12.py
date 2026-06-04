import pygame
import sys
from pygame.locals import QUIT


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello world')
clock = pygame.time.Clock()
tile_size = 16

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


# grma normal
gn = pygame.image.load('assesets/tile_0000.png')
# grama com grama
gg = pygame.image.load('assesets/tile_0001.png')
# grama com flor
gf = pygame.image.load('assesets/tile_0002.png')
# pedra
pd = pygame.image.load('assesets/tile_0043.png')
# partes cerca
ec = pygame.image.load('assesets/tile_0044.png')
ce = pygame.image.load('assesets/tile_0045.png')
dc = pygame.image.load('assesets/tile_0046.png')
cb = pygame.image.load('assesets/tile_0056.png')
pc = pygame.image.load('assesets/tile_0070.png')
pe = pygame.image.load('assesets/tile_0068.png')
# parte casa(telhado)
tl = pygame.image.load('assesets/tile_0052.png')
te = pygame.image.load('assesets/tile_0053.png')
th = pygame.image.load('assesets/tile_0054.png')
tb = pygame.image.load('assesets/tile_0064.png')
tm = pygame.image.load('assesets/tile_0065.png')
td = pygame.image.load('assesets/tile_0066.png')
# parte casa(frente)
di = pygame.image.load('assesets/tile_0076.png')
es = pygame.image.load('assesets/tile_0079.png')
po = pygame.image.load('assesets/tile_0089.png')
ja = pygame.image.load('assesets/tile_0088.png')
# arvore
ab = pygame.image.load('assesets/tile_0016.png')
ac = pygame.image.load('assesets/tile_0004.png')


tiles_img = {
    'gn': gn,
    'gg': gg,
    'gf': gf,
    'pd': pd,
    'ec': ec,
    'ce': ce,
    'dc': dc,
    'cb': cb,
    'pc': pc,
    'pe': pe,
    'tl': tl,
    'te': te,
    'th': th,
    'tb': tb,
    'tm': tm,
    'td': td,
    'di': di,
    'es': es,
    'po': po,
    'ja': ja,
    'ab': ab,
    'ac': ac,
}

mapa = [
    'gg,gg,gg,gg,gn,gn,gg,gg,gg,gg,gg,gg,gf,gn',
    'gn,gf,gg,gg,gf,gf,gg,gf,gf,gg,gg,gf,gn,gn',
    'gn,gn,gg,gg,gg,gg,gf,gf,gf,gg,gf,gf,gf,gf',
    'gg,gg,gg,gg,gf,gg,gg,gf,gf,gg,gf,gf,gg,gf',
    'gn,gg,gg,gg,gf,gg,gf,gg,gg,gf,gf,gn,gg,gg',
    'gg,gf,gf,gg,pd,pd,pd,gf,gg,gf,gg,gf,gn,gg',
    'gf,gn,gg,pd,pd,gf,gg,gf,gf,gg,gf,gg,gg,gn',
    'gg,gg,pd,pd,gg,gf,gg,gg,gf,gf,gf,gg,gg,gf',
    'gg,gg,gn,gf,gn,gg,gf,gg,gf,gf,gn,gf,gg,gg',
    'gf,gf,gf,gg,gg,gg,gf,gf,gg,gg,gn,gg,gf,gn',
]

mapa2 = [
    'ec,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,dc',
    'cb, , , , ,tl,te,th, , , , ,          ,cb',
    'cb,ac, ,ac, ,tb,tm,td, , , , ,        ,cb',
    'cb,ab, ,ab, ,di,ja,es, , , ,ac,       ,cb',
    'cb, , , , ,di,po,es, , , ,ab,         ,cb',
    'cb, ,ac, , , , , , , , , ,            ,cb',
    'cb, ,ab, , , , , , , , , ,            ,cb',
    'cb, , , , , , , , ,ac , , ,           ,cb',
    'cb, , , , , , , , , ab, , ,           ,cb',
    'pe,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,ce,pc',
]


# posicionar o mapa no meio da tela
colunas = len(mapa[0].split(','))
linhas = len(mapa)
offset_x = (800 - colunas * tile_size) // 2
offset_y = (600 - linhas * tile_size) // 2


tipos_solidos = {'ec', 'ce', 'dc', 'cb', 'pc', 'pe', 'tl',
                 'te', 'th', 'tb', 'tm', 'td', 'di', 'es', 'po', 'ja'}

colliders = []
for i in range(len(mapa2)):
    tiles = mapa2[i].split(',')
    for j in range(len(tiles)):
        tile = tiles[j].strip()
        if tile in tipos_solidos:
            colliders.append(pygame.Rect(offset_x + j * tile_size,
                             offset_y + i * tile_size, tile_size, tile_size))


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()
    screen.fill((152, 209, 250))

    # primeiro mapa
    for i in range(len(mapa)):
        tiles = mapa[i].split(',')
        for j in range(len(tiles)):
            tile = tiles[j]
            if tile in tiles_img:
                screen.blit(tiles_img[tile], (offset_x +
                            j * tile_size, offset_y + i * tile_size))

    old_pos_x = pos_x
    old_pos_y = pos_y

    keys = pygame.key.get_pressed()
    movendo = False

    if keys[pygame.K_RIGHT]:
        pos_x = pos_x + 0.1 * dt
        direcao = 'dir'
        movendo = True
    elif keys[pygame.K_LEFT]:
        pos_x = pos_x - 0.1 * dt
        direcao = 'esq'
        movendo = True
    elif keys[pygame.K_UP]:
        pos_y = pos_y - 0.1 * dt
        direcao = 'cima'
        movendo = True
    elif keys[pygame.K_DOWN]:
        pos_y = pos_y + 0.1 * dt
        direcao = 'baixo'
        movendo = True

    collider_jogador = pygame.Rect(pos_x, pos_y, 20, 25)
    if collider_jogador.collidelist(colliders) != -1:
        pos_x = old_pos_x
        pos_y = old_pos_y

    if movendo:
        anim_time += dt
        if anim_time / 1000 > 0.15:
            curr_frame = curr_frame + 1
            if curr_frame > 3:
                curr_frame = 0
            anim_time = 0

    else:
        curr_frame = 0

    # pra calcular o tamanho de cada frame
    # sem isso tava ficando tudo cortado, pq as imagens n batiam na msm largura e altura
    img = direcoes[direcao]
    # retornar o tamanho da imagem
    larg, alt = hero_sprite.get_size()
    frame_larg = larg // 4
    frame_alt = alt // 4
    # diminuir o tamanho so pra ficar mais bonitinho na imagem
    frame_rect = (curr_frame * frame_larg, img *
                  frame_alt, frame_larg, frame_alt)
    # vou recortar o frame
    frame = hero_sprite.subsurface(frame_rect)
    # vou alterar para o tamanho q eu quero
    frame = pygame.transform.scale(frame, (20, 25))
    screen.blit(frame, (pos_x, pos_y))

    # segundo mapa(colocar o segundo mapa aq, para o personagem passar atras das arvores)
    for i in range(len(mapa2)):
        tiles = mapa2[i].split(',')
        for j in range(len(tiles)):
            tile = tiles[j].strip()
            if tile in tiles_img:
                screen.blit(tiles_img[tile], (offset_x +
                            j * tile_size, offset_y + i * tile_size))

    # ver os colliders
    #for collider in colliders:
    #    pygame.draw.rect(screen, (255, 0, 0), collider, 2)
    #pygame.draw.rect(screen, (255, 0, 0), (pos_x, pos_y, 20, 25))
    #pygame.draw.rect(screen, (0, 0, 255), collider_jogador, 2)
    
    pygame.display.update()
