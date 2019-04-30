import os
import random

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Bomb(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image('bomb.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(0, height - self.rect.height)

    def blow_up(self, pos):
        if self.rect.x <= pos[0] <= self.rect.x + self.rect.width and \
                self.rect.y <= pos[1] <= self.rect.y + self.rect.height:
            self.image = pygame.transform.scale(load_image('boom.png'), (50, 50))


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

running = True
fps = 60
v = 100
all_sprites = pygame.sprite.Group()
for i in range(30):
    Bomb(all_sprites)
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for s in all_sprites:
                s.blow_up(event.pos)

    all_sprites.draw(screen)
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
