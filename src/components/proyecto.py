import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, WHITE, DELAY, RUTA_IMAGEN_ELMO, RUTA_IMAGEN_RANA, RUTA_IMAGEN_PIGGY, RUTA_IMAGEN_GALLETA, RUTA_IMAGEN_PIGGY_LOVE
from elements import Personaje, draw_matrix, draw_wall
from handlers import pygame_events
from logic_env import depth_limited_search, breadth_first_search, a_star_search

# Inicializar pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pacman versión Univalle")

# Crear los personajes
rana = Personaje("Rana", RUTA_IMAGEN_RANA, (0, 4))
elmo = Personaje("Elmo", RUTA_IMAGEN_ELMO, (2, 0))
piggy = Personaje("Piggy", RUTA_IMAGEN_PIGGY, (2, 3))
galleta = Personaje("Galleta", RUTA_IMAGEN_GALLETA, (1, 2))

def drawAndFill(window):
    window.fill(WHITE)
    draw_matrix(window)
    draw_wall(window, BLACK)
    # Colocar personajes
    rana.draw(window)
    piggy.draw(window)
    galleta.draw(window)
    elmo.draw(window)
    pygame.display.flip()
    pygame.time.delay(DELAY)

pause = False
isChanged = False

def toggleImg():
    global isChanged
    if isChanged:
        piggy.changeImage(RUTA_IMAGEN_PIGGY)
    else:
        piggy.changeImage(RUTA_IMAGEN_PIGGY_LOVE)
    isChanged = not isChanged

# Bucle principal del juego
while True:
    pygame_events()

    # Dibujar fondo, cuadrícula y muros
    drawAndFill(window)

    # Si se ha ha encontrado algo se pausa el juego
    if pause:
        continue

    # Lógica de búsqueda de la rana
    depth = 6 
    path = depth_limited_search(rana.position, elmo.position, depth)

    if path is not None:
        print("Rana René encontró a Elmo en:", path)

        # Reproducir los movimientos
        for position in path:
            if position == path[0]: # Si es la primera posición
                continue 
            rana.move(position)
            drawAndFill(window)

            if rana.position == elmo.position:
                print("Rana René ha encontrado a Elmo.")
                pause = True

            path_piggy = a_star_search(piggy.position, rana.position, galleta.position)

            # Piggy tiene un 40% de probabilidad de cambiar de imagen y buscar por A*
            # if random.random() < 1:
            #     path_piggy = a_star_search(piggy.position, rana.position, galleta.position)
            #     toggleImg()



            if path_piggy is not None:
                print("Piggy encontró a Rana en:", path_piggy)

                # Reproducir los movimientos dando un paso, es decir desde la posición actual a la siguiente [0] -> [1]
                for position_piggy in path_piggy:
                    if position_piggy == path_piggy[1] and not pause:
                        piggy.move(position_piggy)
                        drawAndFill(window)
                        if piggy.position == elmo.position:
                            print("Piggy ha encontrado a Rana.")
                            pause = True
    else:
        print("Rana René no pudo encontrar a Elmo.")