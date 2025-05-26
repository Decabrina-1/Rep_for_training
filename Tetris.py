import pygame
import sys
import random

# Константы
WIDTH = 10
HEIGHT = 20
CELL_SIZE = 30
SCREEN_WIDTH = WIDTH * CELL_SIZE
SCREEN_HEIGHT = HEIGHT * CELL_SIZE

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 0, 0),
    (244, 67, 54),    # красный
    (156, 39, 176),   # фиолетовый
    (63, 81, 181),    # синий
    (255, 235, 59),   # желтый
    (76, 175, 80),    # зеленый
    (255, 87, 34),    # оранжевый
    (33, 150, 243)    # голубой
]

# Формы тетрамино
SHAPES = [
    # I-форма
    [
        [(0, -1), (0, 0), (0, 1), (0, 2)],  # вертикальная
        [(-1, 0), (0, 0), (1, 0), (2, 0)]   # горизонтальная
    ],
    # Z-форма
    [
        [(0, 0), (1, 0), (0, 1), (-1, 1)],
        [(0, 0), (1, 0), (1, 1), (2, 1)]
    ],
    # S-форма
    [
        [(0, 0), (-1, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (1, -1), (2, 0)]
    ],
    # J-форма
    [
        [(0, -1), (0, 0), (0, 1), (-1, 1)],
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        [(0, 0), (0, 1), (0, -1), (1, -1)],
        [(0, 0), (-1, 0), (-2, 0), (-2, -1)]
    ],
    # L-форма
    [
        [(0, -1), (0, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (2, 0), (2, -1)],
        [(0, 0), (0, 1), (0, -1), (-1, -1)],
        [(0, 0), (-1, 0), (-2, 0), (-2, 1)]
    ],
    # T-форма
    [
        [(0, -1), (0, 0), (0, 1), (1, 0)],
        [(0, 0), (1, 0), (0, 1), (-1, 0)],
        [(0, 0), (0, 1), (0, -1), (-1, 0)],
        [(0, 0), (-1, 0), (0, -1), (1, 0)]
    ],
    # O-форма
    [
        [(0, 0), (1, 0), (0, 1), (1, 1)]
    ]
]

class Figure:
    def __init__(self, x, y, shape_index):
        self.x = x
        self.y = y
        self.shape_index = shape_index
        self.rotation = 0
        self.shape = SHAPES[shape_index]
        self.color = COLORS[self.shape_index + 1]

    def get_blocks(self):
        current_shape = self.shape[self.rotation]
        blocks = []
        for (dx, dy) in current_shape:
            block_x = self.x + dx
            block_y = self.y + dy
            blocks.append((block_x, block_y))
        return blocks

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
        self.current_figure = self.new_figure()
        self.next_figure = self.new_figure()
        self.score = 0
        self.level = 1
        self.fall_speed = 500  # milliseconds
        self.last_fall_time = pygame.time.get_ticks()

    def new_figure(self):
        shape_index = random.randint(0, len(SHAPES) - 1)
        start_x = WIDTH // 2 - 1
        start_y = -1  # Начинаем выше экрана
        return Figure(start_x, start_y, shape_index)

    def draw_grid(self):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if self.grid[y][x]:
                    pygame.draw.rect(self.screen, COLORS[self.grid[y][x]], rect)
                else:
                    pygame.draw.rect(self.screen, BLACK, rect, 1)

    def draw_figure(self, figure):
        for (x, y) in figure.get_blocks():
            if y < 0:
                continue  # игнорируем блоки за верхней границей при отображении
            rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, figure.color, rect)

    def check_collision(self, figure, x, y, rotation):
        temp_figure = Figure(x, y, figure.shape_index)
        temp_figure.rotation = rotation
        for (block_x, block_y) in temp_figure.get_blocks():
            if block_x < 0 or block_x >= WIDTH:
                return True
            if block_y >= HEIGHT:
                return True
            if block_y < 0:
                continue  # допускается, если часть фигуры за верхней границей при начале
            if self.grid[block_y][block_x] != 0:
                return True
        return False

    def lock_figure(self):
        for (x, y) in self.current_figure.get_blocks():
            if y < 0:  # если часть фигуры за верхней границей — game over
                self.game_over()
                return
            self.grid[y][x] = self.current_figure.shape_index + 1
        self.current_figure = self.next_figure
        self.next_figure = self.new_figure()
        self.check_lines()

    def check_lines(self):
        lines = 0
        for y in range(HEIGHT):
            if all(self.grid[y]):
                del self.grid[y]
                self.grid.insert(0, [0]*WIDTH)
                lines +=1
        if lines >0:
            self.score += lines * 100

    def game_over(self):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not self.check_collision(self.current_figure, self.current_figure.x -1, self.current_figure.y, self.current_figure.rotation):
                        self.current_figure.x -=1
                elif event.key == pygame.K_RIGHT:
                    if not self.check_collision(self.current_figure, self.current_figure.x +1, self.current_figure.y, self.current_figure.rotation):
                        self.current_figure.x +=1
                elif event.key == pygame.K_DOWN:
                    self.fall_speed = 100  # ускорить падение
                elif event.key == pygame.K_UP:
                    new_rotation = (self.current_figure.rotation +1) % len(self.current_figure.shape)
                    if not self.check_collision(self.current_figure, self.current_figure.x, self.current_figure.y, new_rotation):
                        self.current_figure.rotation = new_rotation
                elif event.key == pygame.K_SPACE:
                    while not self.check_collision(self.current_figure, self.current_figure.x, self.current_figure.y +1, self.current_figure.rotation):
                        self.current_figure.y +=1
                    self.lock_figure()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_fall_time > self.fall_speed:
            if not self.check_collision(self.current_figure, self.current_figure.x, self.current_figure.y +1, self.current_figure.rotation):
                self.current_figure.y +=1
                self.last_fall_time = current_time
            else:
                self.lock_figure()
                self.last_fall_time = current_time

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.screen.fill(BLACK)
            self.draw_grid()
            self.draw_figure(self.current_figure)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()