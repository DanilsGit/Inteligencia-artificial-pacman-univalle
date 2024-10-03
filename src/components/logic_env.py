import heapq
from config import TAM_SQUARE
from elements import is_wall

# Función para obtener los movimientos válidos de una posición
def get_valid_moves(position):
    # Retorna una lista de movimientos válidos desde la posición actual
    valid_moves = []
    potential_moves = [
        (position[0] - 1, position[1]),  # Arriba
        (position[0], position[1] - 1),  # Izquierda
        (position[0] + 1, position[1]),  # Abajo
        (position[0], position[1] + 1),   # Derecha
    ]

    for move in potential_moves:
        if not is_wall(move):
            valid_moves.append(move)

    return valid_moves

# búsqueda limitada por profundidad
def depth_limited_search(current_position, goal_position, depth, path=None):
    if path is None:
        path = []

    # Añadir la posición actual al camino
    path.append(current_position)

    # Comprobar si hemos llegado al objetivo
    if current_position == goal_position:
        return path  # Retorna el camino completo al objetivo

    # Si se alcanza la profundidad máxima, retornar None
    if depth <= 0:
        path.pop()  # Retrocede antes de retornar None
        return None

    # Obtener movimientos válidos
    for move in get_valid_moves(current_position):
        new_path = depth_limited_search(move, goal_position, depth - 1, path)
        if new_path is not None:
            return new_path  # Retorna la ruta encontrada

    # Retroceder si no se encontró una ruta
    path.pop()  # Retrocede si no se encontró una ruta
    return None  # No se encontró una ruta

#Busqueda por amplitud
def breadth_first_search(current_position, goal_position):
    # Crear una cola para almacenar los nodos a visitar
    queue = [[current_position]]

    # Crear un conjunto para almacenar los nodos visitados
    visited = set()

    # Mientras la cola no esté vacía
    while queue:
        # Obtener el camino actual
        path = queue.pop(0)

        # Obtener la posición actual
        current_position = path[-1]

        # Si la posición actual es el objetivo, retornar el camino
        if current_position == goal_position:
            return path

        # Si la posición actual no ha sido visitada
        if current_position not in visited:
            # Marcar la posición actual como visitada
            visited.add(current_position)

            # Obtener los movimientos válidos
            for move in get_valid_moves(current_position):
                # Crear un nuevo camino
                new_path = list(path)
                new_path.append(move)

                # Añadir el nuevo camino a la cola
                queue.append(new_path)

    # Si no se encontró un camino, retornar None
    return None

# Búsqueda por A*
def a_star_search(start, goal):
    """
    Implementación de la búsqueda A*.
    
    Args:
    - start: posición inicial (tupla con fila, columna)
    - goal: posición del objetivo (tupla con fila, columna)
    
    Retorna:
    - path: lista de posiciones que componen la ruta encontrada.
    """

    # Prioridad de la cola (heap) para almacenar nodos a explorar
    open_list = []
    heapq.heappush(open_list, (0, start))  # (f(n), posición)

    # Diccionarios para mantener el rastro de nodos explorados
    came_from = {}  # Para reconstruir la ruta
    g_score = {start: 0}  # Costo acumulado desde el inicio hasta cada nodo

    # Almacenar la distancia mínima esperada hasta el objetivo
    f_score = {start: heuristic(start, goal)}

    while open_list:
        # Extraer el nodo con menor f(n)
        _, current = heapq.heappop(open_list)

        # Si hemos alcanzado el objetivo, reconstruir la ruta
        if current == goal:
            return reconstruct_path(came_from, current)

        # Explorar los movimientos posibles
        for neighbor in get_valid_moves(current):
            tentative_g_score = g_score[current] + 1  # Costo de moverse al vecino (siempre 1)

            # Si el vecino no está en g_score o encontramos una ruta más corta
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                # Guardar el mejor camino hasta el momento
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)

                # Añadir el vecino a la lista si no está ya en la cola
                if neighbor not in [i[1] for i in open_list]:
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    # Si no se encuentra una ruta
    return None

def heuristic(pos1, pos2):
    """
    Heurística para estimar la distancia entre dos posiciones (Distancia de Manhattan).
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def reconstruct_path(came_from, current):
    """
    Reconstruir la ruta desde el diccionario de posiciones exploradas.
    """
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path