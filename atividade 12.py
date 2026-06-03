import pygame, sys
from pygame.locals import QUIT


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello world')
clock = pygame.time.Clock()
tile_size = 16


#grma normal
gn = pygame.image.load('tile_0000.png')
#grama com grama
gg = pygame.image.load('tile_0001.png')
#grama com flor
gf = pygame.image.load('tile_0002.png')
#pedra
pd = pygame.image.load('title_0043.png')

mapa = [
    'gngngngngngngngngngngngngngn',
    'gngfgngngngfgggngngngngfgngn',
    'gngngggngngggngngngngngngngf',
    'gngngggngngngngngpdgngngngn',
    'gngngngngngngngnpdpdgngngggn',
    'gngfgngngngngnpdpdgngngngngn',
    'gngngggngfgnggpdgfgngfgngngn',
    'gngggngngggnggpdgngngngggngn',
    'gngngngfgngngngngngngngngngn',
    'gngfgngngngngngngngngngngngn',
]

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    clock.tick(60)
    dt = clock.get_time()

    for i in range(len(mapa)):
        for j in range(len(mapa)):
            if mapa[i][j] == 'gn':
                screen.blit(gn, (j*tile_size, i*tile_size),(0, 0, tile_size, tile_size))
            elif mapa[i][j] == 'gg':
                screen.blit(gg, (j*tile_size, i*tile_size),(16, 0, tile_size, tile_size))
            elif mapa[i][j] == 'gf':
                screen.blit(gf, (j*tile_size, i*tile_size),(32, 0, tile_size, tile_size))
            elif mapa[i][j] == 'pd':
                screen.blit(gf, (j*tile_size, i*tile_size),(48, 0, tile_size, tile_size))









    pygame.display.update()