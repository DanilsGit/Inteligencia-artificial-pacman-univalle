# Elementos

import pygame
from config import TAM_SQUARE, BLACK, WALLS, WINDOW_HEIGHT, WINDOW_WIDTH
from utils import load_img

class Personaje:
    def __init__(self, name, img_url, initial_pos):
        self.name = name
        self.img = load_img(img_url, (TAM_SQUARE, TAM_SQUARE))
        self.position = initial_pos

    def changeImage(self, img_url):
        self.img = load_img(img_url, (TAM_SQUARE, TAM_SQUARE))
    
    def draw(self, window):
        x = self.position[1] * TAM_SQUARE
        y = self.position[0] * TAM_SQUARE
        window.blit(self.img, (x, y))

    def move(self, new_pos):
        if not is_wall(new_pos):
            self.position = new_pos

# Función para verificar si una posición es un muro
def is_wall(position):
    if (position[0] < 0 or position[0] >= 4) or (position[1] < 0 or position[1] >= 5):
        return True
    return position in WALLS

# Función para draw los muros en la window
def draw_wall(window, color=(0, 0, 255)):
    for wall in WALLS:
        x = wall[1] * TAM_SQUARE
        y = wall[0] * TAM_SQUARE
        pygame.draw.rect(window, color, (x, y, TAM_SQUARE, TAM_SQUARE))

# Función para draw la cuadrícula
def draw_matrix(window):
    for row in range(int(WINDOW_HEIGHT/TAM_SQUARE)):
        for col in range(int(WINDOW_WIDTH/TAM_SQUARE)):
            pygame.draw.rect(window, BLACK, (col * TAM_SQUARE, row * TAM_SQUARE, TAM_SQUARE, TAM_SQUARE), 1)
