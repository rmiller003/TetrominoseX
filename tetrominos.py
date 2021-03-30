import pygame
import random

pygame.font.init()

screen_width=790
screen_height=690
display_width=300
display_height=590

block_size=30

x_topleft=(screen_width - display_width) //2
y_topleft= screen_height - display_height

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]


Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

S = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]


L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

J = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00..',
      '.....']]


blocks = [T, Z, S, O, I, L, J]
blocks_colors = [(0, 255, 0), (255, 0, 0), (0, 255,255), (255,255,0), (255,165,0),(0,0,255), (128,0,128)]

def lost_blocks(positions):
    for position in positions:
        x, y = position
        if y < 1:
            return True
    return False

def obtain_shape():
    global blocks, blocks_colors

    return BLOCK(5, 0, random.choice(blocks))

class BLOCK(object):
    rows = 20
    columns = 10

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = blocks_colors[blocks.index(shape)]
        self.rotation = 0

def make_grid(lock_positions={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in lock_positions:
                c = lock_positions[(j,i)]
                grid[i][j] = c
    return grid


def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (x_topleft + display_width/2 - (label.get_width() / 2), y_topleft + display_height/2 - label.get_height()/))



def main_program():
    global grid()

    lock_position ={}
    grid= make_grid(lock_position)

    change_block = False
    run=True
    current_block = obtain_shape()
    next_block = obtain_shape()
    clock = pygame.time.Clock()
    fall_time=0

    while run:
        fall_speed = 0.27

        grid=make_grid(lock_position)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_block.y += 1
            if not (space_valid(current_block, grid)) and current_block.y > 0:
                current_block.y -= 1
                change_block = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT
                run = False
                pygame.display.quit()
                quit()

def main_window():
    run = True
    while run:
        root.fill((0,0,0))
        draw_text_middle('Press any key to start...',59,(255,255,0),root)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                main_program()
    pygame.QUIT()

