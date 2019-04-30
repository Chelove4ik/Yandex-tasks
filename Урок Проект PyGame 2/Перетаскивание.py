import pygame

pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)

running = True
delta = (0, 0)
x, y, = 0, 0
moving = False

clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if x <= event.pos[0] <= x + 100 and y <= event.pos[1] <= y + 100:
                moving = True
                delta = (event.pos[0] - x, event.pos[1] - y)
        if event.type == pygame.MOUSEMOTION:
            if moving:
                x, y = event.pos[0] - delta[0], event.pos[1] - delta[1]
        if event.type == pygame.MOUSEBUTTONUP:
            moving = False

    pygame.draw.rect(screen, (0, 255, 0), (x, y, 100, 100))

    pygame.display.flip()
    clock.tick(60)
