import pyautogui
import random
import time

def mover_cursor_aleatoriamente(duracion, intervalo):
    """
    Mueve el cursor en direcciones aleatorias durante un tiempo especificado.

    :param duracion: Duración total en segundos para mover el cursor.
    :param intervalo: Intervalo en segundos entre cada movimiento.
    """
    tiempo_inicial = time.time()
    while time.time() - tiempo_inicial < duracion:
        # Obtener el tamaño de la pantalla
        ancho_pantalla, alto_pantalla = pyautogui.size()

        # Generar nuevas coordenadas aleatorias dentro de los límites de la pantalla
        nueva_x = random.randint(0, ancho_pantalla - 1)
        nueva_y = random.randint(0, alto_pantalla - 1)

        # Mover el cursor a las nuevas coordenadas
        pyautogui.moveTo(nueva_x, nueva_y, duration=intervalo)

        # Esperar un intervalo antes del siguiente movimiento
        time.sleep(intervalo)

if __name__ == "__main__":
    duracion = 30  # Duración total en segundos
    intervalo = 0.5  # Intervalo en segundos entre cada movimiento
    mover_cursor_aleatoriamente(duracion, intervalo)