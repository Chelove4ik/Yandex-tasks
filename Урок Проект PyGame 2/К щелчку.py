import pygame

running = True
num = 1

pygame.init()

size = width, height = 501, 501

screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))

cx, cy, ex, ey = 250, 250, 250, 250

clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True  # включаем режим рисования
            # запоминаем координаты одного угла
            ex, ey = event.pos

    if cx < ex:
        cx += 1
    elif cx > ex:
        cx -= 1

    if cy < ey:
        cy += 1
    elif cy > ey:
        cy -= 1

    pygame.draw.circle(screen, (255, 0, 0), (cx, cy), 20)

    pygame.display.flip()
    screen.fill((0, 0, 0))
    clock.tick(60)
