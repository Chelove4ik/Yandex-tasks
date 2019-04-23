import os

import pygame
import requests
from distance import lonlat_distance

data = [(30.206151, 59.919913), (30.258248, 59.917525), (30.267206, 59.919417),
        (30.275123, 59.931089), (30.310724, 59.941660), (30.312958, 59.940869)]

data_f = ','.join([','.join(list(map(str, p))) for p in data])
point = ','.join(list(map(str, data[len(data) // 2])))
s = 0
for p in range(len(data)):
    if p != len(data) - 1:
        s += lonlat_distance(data[p], data[p + 1])

response = [('Metro',
             f'https://static-maps.yandex.ru/1.x/?l=map&pl=c:8822DDC0,w:5,{data_f}&pt={point},pm2wtm1')]

for resp in response:
    with open(f'{resp[0]}.png', mode='wb') as f:
        f.write(requests.get(resp[1]).content)

pygame.init()
size = width, height = 600, 500
screen = pygame.display.set_mode(size)
running = True

map_file = 'Metro.png'
img = pygame.image.load(map_file)

myfont = pygame.font.SysFont('arial', 30)
metr = myfont.render(str(int(s)) + 'm', 1, (255, 255, 255))

screen.blit(img, (0, 50))
screen.blit(metr, (5, 5))

pygame.display.flip()
clock = pygame.time.Clock()
while pygame.event.wait().type != pygame.QUIT:
    clock.tick(30)
pygame.quit()

os.remove(map_file)
