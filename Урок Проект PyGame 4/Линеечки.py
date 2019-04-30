from pprint import pprint

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
                if self.board[y][x] == 1:
                    pygame.draw.circle(screen, (0, 0, 255),
                                       (self.left + x * self.cell_size + self.cell_size // 2,
                                        self.top + y * self.cell_size + self.cell_size // 2), self.cell_size // 2)
                elif self.board[y][x] == 2:
                    pygame.draw.circle(screen, (255, 0, 0),
                                       (self.left + x * self.cell_size + self.cell_size // 2,
                                        self.top + y * self.cell_size + self.cell_size // 2), self.cell_size // 2)
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


class Lines(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.moves = []
        self.red = False

    def place_ball(self, x, y):
        if not self.red:
            self.board[x][y] = 1
        else:
            if self.has_path(self.red[0], self.red[1], x, y):
                self.board[x][y] = 1
                self.board[self.red[0]][self.red[1]] = 0
                self.red = False

    def make_red_ball(self, x, y):
        if not self.red and self.board[x][y] == 1:
            self.board[x][y] = 2
            self.red = (x, y)
        elif self.red and self.board[x][y] == 2:
            self.board[x][y] = 1
            self.red = False

    def has_path(self, x1, y1, x2, y2):
        field = [[0] * len(self.board[0]) for _ in range(len(self.board))]
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 1:
                    field[i][j] = 10 ** 9
        # pprint(field)

        N = len(self.board[0])
        q = [(x1 + 1, y1 + 1, 0)]  # 1st and 2nd coordinates x, y, 3rd is number of steps to the cell
        while len(q) != 0:
            cur = q.pop(0)
            field[cur[0]][cur[1]] = cur[2]
            if cur[0] + 1 < N and field[cur[0] + 1][cur[1]] < 1 and (cur[0] + 1, cur[1], cur[2] + 1) not in q:
                q.append((cur[0] + 1, cur[1], cur[2] + 1))
            if cur[1] + 1 < N and field[cur[0]][cur[1] + 1] < 1 and (cur[0], cur[1] + 1, cur[2] + 1) not in q:
                q.append((cur[0], cur[1] + 1, cur[2] + 1))
            if cur[0] - 1 >= 0 and field[cur[0] - 1][cur[1]] < 1 and (cur[0] - 1, cur[1], cur[2] + 1) not in q:
                q.append((cur[0] - 1, cur[1], cur[2] + 1))
            if cur[1] - 1 >= 0 and field[cur[0]][cur[1] - 1] < 1 and (cur[0], cur[1] - 1, cur[2] + 1) not in q:
                q.append((cur[0], cur[1] - 1, cur[2] + 1))
            if (cur[0], cur[1]) == (x2, y2):
                return True
        pprint(field)


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

running = True
fps = 60
v = 100
board = Lines(9, 9)
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            try:
                y, x = board.get_cell(event.pos)
            except TypeError:
                break
            if event.button == 1:
                board.place_ball(x, y)
            elif event.button == 3:
                board.make_red_ball(x, y)
                pass

    board.render()

    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
