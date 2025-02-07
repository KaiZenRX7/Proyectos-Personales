import json
from Programas.morse_dict import MORSE_CODE_DICT
import winsound
import time

HISTORIAL_FILE = 'historial.json'

DURATION_DOT = 100
DURATION_DASH = 300
FREQUENCY = 750


def cargar_historial():
    try:
        with open(HISTORIAL_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
    

def guardar_historial(historial):
    with open(HISTORIAL_FILE, 'w') as file:
        json.dump(historial, file, indent =4)

def traducir_a_morse(texto):
    texto = texto.upper()
    morse = ' '.join(MORSE_CODE_DICT.get(char, '') if char != ' ' else '/' for char in texto)
    return morse

def reproducir_morse(morse):
    for char in morse:
        if char == '.':
            winsound.Beep(FREQUENCY, DURATION_DOT)
        elif char == '-':
            winsound.Beep(FREQUENCY, DURATION_DASH)
        elif char == '/':
            time.sleep(0.7)
        else:
            time.sleep(0.5)

def mostrar_menu():
    print("1. Traducir texto a morse")
    print("2. Mostrar historial")
    print("3. Salir")

def main():
    historial = cargar_historial()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            palabra = input("Ingrese el texto a traducir: ")
            traduccion = traducir_a_morse(palabra)
            print(f"Traduccion a morse : {traduccion}")
            reproducir_morse(traduccion)
            historial[palabra] = traduccion
            guardar_historial(historial)
        elif opcion == '2':
            print("Historial de traducciones:")
            for palabra, traduccion in historial.items():
                print(f"{palabra}: {traduccion}")
        elif opcion == '3':
            print("Saliendo del programa...")
            despedida = traducir_a_morse("Hasta luego")
            reproducir_morse(despedida)
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()