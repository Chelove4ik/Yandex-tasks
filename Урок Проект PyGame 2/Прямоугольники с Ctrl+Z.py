import pygame

from pygame.constants import K_z, KMOD_LCTRL

running = True
num = 1

pygame.init()

size = width, height = 500, 500

screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))

screen2 = pygame.Surface(screen.get_size())
x1, y1 = 0, 0

screens = [screen2]

drawing = False  # режим рисования выключен
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True  # включаем режим рисования
            # запоминаем координаты одного угла
            x1, y1 = event.pos
            w, h = event.pos[0] - x1, event.pos[1] - y1
        if event.type == pygame.MOUSEBUTTONUP:
            # сохраняем нарисованное (на втором холсте)
            screen2 = pygame.Surface(screen.get_size())
            screen2.blit(screen, (0, 0))
            screens.append(screen2)
            drawing = False
        if event.type == pygame.MOUSEMOTION:
            # запоминаем текущие размеры
            w, h = event.pos[0] - x1, event.pos[1] - y1
        if event.type == pygame.KEYDOWN and event.key == K_z and pygame.key.get_mods() == KMOD_LCTRL:
            try:
                screens = screens[:-1:]
            except Exception:
                pass
    # рисуем на экране сохранённое на втором холсте
    screen.fill((0, 0, 0))
    try:
        screen.blit(screens[-1], (0, 0))
    except Exception:
        pass
    if drawing:  # и, если надо, текущий прямоугольник
        pygame.draw.rect(screen, (255, 255, 255), ((x1, y1), (w, h)), 5)

    pygame.display.flip()
