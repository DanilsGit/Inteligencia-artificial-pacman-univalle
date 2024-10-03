import pygame

# Función para cargar imágenes y redimensionarlas
def load_img(url, size):
    imagen = pygame.image.load(url)
    return pygame.transform.scale(imagen, size)
