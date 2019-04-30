import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(platforms)
        self.x = x
        self.y = y
        self.width = 50
        self.height = 10
        self.image = pygame.Surface((self.width, self.height))
        pygame.draw.rect(self.image, pygame.Color('grey'), (0, 0, self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class Ladder(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(ladders)
        self.x = x
        self.y = y
        self.width = 10
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        pygame.draw.rect(self.image, pygame.Color('red'), (0, 0, self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(player)
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.image = pygame.Surface((self.width, self.height))
        pygame.draw.rect(self.image, pygame.Color('blue'), (0, 0, self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.vy = 1
        self.l = False

    def update(self):
        if len(pygame.sprite.spritecollide(self, platforms, False)) == 0 and len(
                pygame.sprite.spritecollide(self, ladders, False)) == 0:
            self.vy = 1
        else:
            self.vy = 0
        if len(pygame.sprite.spritecollide(self, ladders, False)) != 0:
            self.l = True
        else:
            self.l = False
        self.rect = self.rect.move(0, self.vy)


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

running = True
fps = 50
v = 100
platforms = pygame.sprite.Group()
player = pygame.sprite.Group()
ladders = pygame.sprite.Group()
pl = None
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.key.get_mods() & pygame.KMOD_CTRL and event.button == 1:
                Ladder(event.pos[0], event.pos[1])
            elif event.button == 1:
                Platform(event.pos[0], event.pos[1])
            elif event.button == 3:
                player = pygame.sprite.Group()
                pl = Player(event.pos[0], event.pos[1])
        if event.type == pygame.KEYDOWN:
            if pl is not None:
                if event.key == pygame.K_RIGHT:
                    pl.rect = pl.rect.move(10, 0)
                if event.key == pygame.K_LEFT:
                    pl.rect = pl.rect.move(-10, 0)
                if event.key == pygame.K_DOWN and pl.l:
                    pl.rect = pl.rect.move(0, 10)
                if event.key == pygame.K_UP and pl.l:
                    pl.rect = pl.rect.move(0, -10)

    platforms.draw(screen)
    ladders.draw(screen)
    player.draw(screen)
    player.update()
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
