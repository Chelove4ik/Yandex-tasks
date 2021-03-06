import os

import pygame

from requests import get

num = 0
names = []


def get_photo(url):
    global num, names
    num += 1
    photo = get(url)
    if photo.status_code != 400:
        map_file = f"maps{str(num)}.jpg"
        names.append(map_file)
        try:
            with open(map_file, "wb") as file:
                file.write(photo.content)
        except IOError as ex:
            print("Ошибка записи временного файла:", ex)
            exit(2)


lst = [
    'https://static-maps.yandex.ru/1.x/?ll=131.900632%2C43.027252&spn=0.02,0.02&l=sat',
    'https://static-maps.yandex.ru/1.x/?ll=37.681544%2C55.754262&spn=0.2,0.2&l=sat',
    'https://static-maps.yandex.ru/1.x/?ll=30.465586%2C59.921371&spn=0.2,0.2&l=sat'
]
for i in lst:
    get_photo(i)

pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.flip()

myfont = pygame.font.SysFont('arial', 15)
label = myfont.render(lst[0], 1, (255, 255, 255))

clock = pygame.time.Clock()
running = True
number = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            number += 1
            number %= len(names)
            label = myfont.render(lst[number], 1, (255, 255, 255))
    screen.fill((0, 0, 0))

    screen.blit(pygame.image.load(names[number]), (0, 50))
    screen.blit(label, (0, 0))

    clock.tick(30)
    pygame.display.flip()

pygame.quit()

for i in names:
    os.remove(i)
