import pygame
from config import POSICIONES, DEPTH, WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, WHITE, DELAY, RUTA_IMAGEN_BLANCO, RUTA_IMAGEN_ELMO, RUTA_IMAGEN_RANA, RUTA_IMAGEN_PIGGY, RUTA_IMAGEN_GALLETA, RUTA_IMAGEN_PIGGY_LOVE, RUTA_IMAGEN_TRIO, RUTA_IMAGEN_PIGGY_RANA, RUTA_IMAGEN_ELMO_RANA
from elements import Personaje, draw_matrix, draw_wall
from handlers import pygame_events
from logic_env import depth_limited_search, breadth_first_search, a_star_search
from mensaje import mostrar_mensaje
import random

# Inicializar pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pacman versión Univalle")

# Crear los personajes
rana = Personaje("Rana", RUTA_IMAGEN_RANA, POSICIONES[0])
elmo = Personaje("Elmo", RUTA_IMAGEN_ELMO, POSICIONES[1])
piggy = Personaje("Piggy", RUTA_IMAGEN_PIGGY, POSICIONES[2])
galleta = Personaje("Galleta", RUTA_IMAGEN_GALLETA,POSICIONES[3])

def drawAndFill(window):
    window.fill(WHITE)
    draw_wall(window, BLACK)
    # Colocar personajes
    galleta.draw(window)
    rana.draw(window)
    piggy.draw(window)
    elmo.draw(window)
    # Dibujar la matriz
    draw_matrix(window)
    pygame.display.flip()
    pygame.time.delay(DELAY)

pause = False
isChanged = False
isAStart = False

def toggleImg():
    global isChanged
    if isChanged:
        piggy.changeImage(RUTA_IMAGEN_PIGGY)
    else:
        piggy.changeImage(RUTA_IMAGEN_PIGGY_LOVE)
    isChanged = not isChanged

def winGame():
    if piggy.position == rana.position == elmo.position:
    
        elmo.changeImage(RUTA_IMAGEN_TRIO)
        print("TRIO")
        drawAndFill(window)
        mostrar_mensaje("¡Felicidades! Se formó trio")
        return True
        

    if piggy.position == rana.position:
        print("Piggy ha encontrado a Rana.")
        piggy.changeImage(RUTA_IMAGEN_PIGGY_RANA)
        drawAndFill(window)
        mostrar_mensaje("Piggy ha encontrado a Rana")
        return True

    if rana.position == elmo.position:
        print("Rana René ha encontrado a Elmo.")
        elmo.changeImage(RUTA_IMAGEN_ELMO_RANA)
        drawAndFill(window)
        mostrar_mensaje("Rana René ha encontrado a Elmo")
        return True
    
    if piggy.position == galleta.position:
        print("Se comio la galleta")
        galleta.changeImage(RUTA_IMAGEN_BLANCO)
        return False


# Bucle principal del juego
while True:
    pygame_events()

    # Dibujar fondo, cuadrícula y muros
    drawAndFill(window)

    # Si se ha ha encontrado algo se pausa el juego
    if pause:
        continue

    # Lógica de búsqueda de la rana
    path_rana = depth_limited_search(rana.position, elmo.position, DEPTH)

    if path_rana is not None:
        print("Rana René encontró a Elmo en:", path_rana)

        # Reproducir los movimientos de la rana
        for i in range(len(path_rana)):
            if i == 0 or pause: # Si es la primera posición o ya se encontró a Elmo,
                continue

            rana.move(path_rana[i])
            drawAndFill(window)

            if winGame():
                pause = True
                continue

            if not isAStart:
                path_piggy = breadth_first_search(piggy.position, rana.position)

            # Piggy tiene un 40% de probabilidad de cambiar de imagen y buscar por A*
            if random.random() < 0.4 or isAStart:
                path_piggy = a_star_search(piggy.position, rana.position, galleta.position)
                if not isAStart:
                    toggleImg()
                isAStart = True
            

            if path_piggy is not None:
                print("Piggy encontró a Rana en:", path_piggy)
                # Reproducir los movimientos dando un paso, es decir desde la posición actual a la siguiente [0] -> [1]
                if not pause:
                    piggy.move(path_piggy[1])
                    if winGame():
                        pause = True
                        continue
                    drawAndFill(window)
    else:
        print("Rana René no pudo encontrar a Elmo.")
        pause = True