import pygame
# Configuración

# Dimensiones de la window
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
TAM_SQUARE = 200

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Cargar imágenes
RUTA_IMAGEN_ELMO = "./src/images/elmo.png"
RUTA_IMAGEN_RANA = "./src/images/rana.jpg"
RUTA_IMAGEN_PIGGY = "./src/images/cerda.jpg"
RUTA_IMAGEN_PIGGY_LOVE = "./src/images/cerdaLove.jpg"
RUTA_IMAGEN_GALLETA = "./src/images/galleta.jpg"
RUTA_IMAGEN_TRIO = "./src/images/trio.webp"
RUTA_IMAGEN_PIGGY_RANA = "./src/images/ranaYcerda.jpg"
RUTA_IMAGEN_ELMO_RANA = "./src/images/elmoYrana.jpeg"
RUTA_IMAGEN_BLANCO = "./src/images/blanco.png"

# Configuración
DELAY = 1000

# Definir los muros
# Posiciones iniciales RANA, ELMO, PIGGY, GALLETA
POSICIONES = [
            (0, 4), (2, 0), (2, 3), (1, 1)
            #(3,3), (2,0), (2, 4), (3, 2)
            #(0, 2), (2, 2), (3, 4), (3, 3)
            #(0, 3), (2, 2), (2, 0), (3, 3) #si hace A* no encuentra 
            #(1, 2), (2, 3), (3, 3), (3, 4) #si hace A* lo encuentra
            ]

# Definir los muros
WALLS = [
    (3,1), (2,1), (2,2), (1,2)             #6
    #(3,1), (2,1), (2,2), (1,2)             #8
    #(1,3), (1, 1), (1, 2), (3, 0), (3, 1)   #6
    #(1,2), (1, 1), (1, 3), (0, 2), (2, 1),(3,4)  #5
    #(0, 1), (1, 1), (2, 1),(1,3)  #2
]

DEPTH = 6
