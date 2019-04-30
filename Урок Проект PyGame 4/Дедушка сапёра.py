from random import randint

import pygame


class Board:
    def __init__(self, wid, heig):
        self.wid = wid
        self.heig = heig
        self.board = [[0] * wid for _ in range(heig)]
        self.left = 0
        self.top = 0
        self.cell_size = 50

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for y in range(self.wid):
            for x in range(self.heig):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + x * self.cell_size, self.top + y * self.cell_size,
                                  self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        block = (mouse_pos[0] - board.left) // board.cell_size, (mouse_pos[1] - board.top) // board.cell_size
        return block if not (block[0] < 0 or block[0] >= board.wid or block[1] < 0 or block[1] >= board.heig) else None

    def on_click(self, cell_coords):
        block = cell_coords
        if block is not None:
            board.board[block[1]][block[0]] = (board.board[block[1]][block[0]] + 1) % 3

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


class Minesweeper(Board):
    def __init__(self, width, height, screen, mines):
        super().__init__(width + 2, height + 2)
        self.mines = mines
        self.screen = screen
        counter = mines - 1
        while counter >= 0:
            w = randint(1, width - 2)
            h = randint(1, height - 2)
            if self.board[h][w] == 0:
                self.board[h][w] = 10
                counter -= 1

    def render(self):
        for i in range(1, len(self.board) - 1):
            for j in range(1, len(self.board[i]) - 1):
                pygame.draw.rect(self.screen, pygame.Color('white'), (
                    self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size, self.cell_size), 1)
                if self.board[i][j] == 10:
                    pygame.draw.rect(self.screen, pygame.Color('red'), (
                        self.left + 1 + j * self.cell_size, self.top + 1 + i * self.cell_size, self.cell_size - 2,
                        self.cell_size - 2))

    def open_cell(self, pos):
        w, h = self.get_cell(pos)
        counter = 0
        if self.board[h][w + 1] == 10:
            counter += 1
        if self.board[h + 1][w] == 10:
            counter += 1
        if self.board[h + 1][w + 1] == 10:
            counter += 1
        if self.board[h + 1][w - 1] == 10:
            counter += 1
        if self.board[h][w - 1] == 10:
            counter += 1
        if self.board[h - 1][w] == 10:
            counter += 1
        if self.board[h - 1][w + 1] == 10:
            counter += 1
        if self.board[h - 1][w - 1] == 10:
            counter += 1
        show_text(str(counter), w * self.cell_size + self.cell_size // 2, h * self.cell_size + self.cell_size // 2,
                  self.screen)


def show_text(text, x, y, surface, color='white', size=30, align='left'):
    font = pygame.font.Font(None, size)

    string_rendered = font.render(text, 1, pygame.Color(color))
    text_rect = string_rendered.get_rect()
    text_rect.x = x
    text_rect.y = y
    if align == 'center':
        text_rect.x -= text_rect.width // 2
        text_rect.y -= text_rect.height // 2
    pygame.draw.rect(surface, pygame.Color('black'), text_rect)
    surface.blit(string_rendered, text_rect)


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

running = True
fps = 60
v = 100
board = Minesweeper(5, 7, screen, 7)
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.open_cell(event.pos)
        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            rising = True

    board.render()

    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
