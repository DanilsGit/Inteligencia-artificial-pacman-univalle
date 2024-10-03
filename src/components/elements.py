# Elementos

import pygame
from config import TAM_SQUARE, BLACK

class Personaje:
    def __init__(self, name, img_url, initial_pos):
        self.name = name
        self.img = pygame.image.load(img_url)
        self.img = pygame.transform.scale(self.img, (TAM_SQUARE, TAM_SQUARE))
        self.position = initial_pos

    def changeImage(self, img_url):
        self.img = pygame.image.load(img_url)
        self.img = pygame.transform.scale(self.img, (TAM_SQUARE, TAM_SQUARE))
    
    def draw(self, window):
        x = self.position[1] * TAM_SQUARE
        y = self.position[0] * TAM_SQUARE
        window.blit(self.img, (x, y))

    def move(self, new_pos):
        if not is_wall(new_pos):
            self.position = new_pos

# Definir los muros
walls = [
    (4,1), (3,1), (3,2), (2,2)
]

# Función para verificar si una posición es un muro
def is_wall(position):
    if (position[0] < 0 or position[0] >= 4) or (position[1] < 0 or position[1] >= 5):
        return True
    return position in walls

# Función para draw los muros en la window
def draw_wall(window, color=(0, 0, 255)):
    for wall in walls:
        x = wall[1] * TAM_SQUARE
        y = wall[0] * TAM_SQUARE
        pygame.draw.rect(window, color, (x, y, TAM_SQUARE, TAM_SQUARE))

# Función para draw la cuadrícula
def draw_matrix(window):
    for row in range(4):
        for col in range(5):
            pygame.draw.rect(window, BLACK, (col * TAM_SQUARE, row * TAM_SQUARE, TAM_SQUARE, TAM_SQUARE), 1)
