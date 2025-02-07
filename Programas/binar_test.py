import pickle # para cargar el diccionario
import time # para pausar el programa

def cargar_diccionario(filename):
    """
    Carga el diccionario de letras en binario desde un archivo binario.
    El diccionario debe mapear letras a sus códigos en binario (cadena).
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)

def traducir_a_binario(frase, diccionario):
    """
    Traduce una frase a binario usando el diccionario para cada letra.
    Cada letra se traduce a su binario; 
    cuando hay un espacio en la frase, se usa '/'.
    Si un carácter no está en el diccionario, se muestra '?'.
    """
    traduccion = []
    for char in frase.lower():
        if char == ' ':
            traduccion.append('/')
        else:
            traduccion.append(diccionario.get(char, '?'))
    return " ".join(traduccion)

def mostrar_menu():
    print("\nMenu de opciones:")
    print("1. Traducir a binario")
    print("2. Ver historial de traducciones")
    print("3. Salir")

def main():
    diccionario = cargar_diccionario('diccionario_letras.bin')
    historial = {}  # Almacena traducciones: {frase: traduccion}
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")
        if opcion == '1':
            frase = input("Ingrese la palabra o frase a traducir: ")
            traduccion = traducir_a_binario(frase, diccionario)
            print(f"Traducción: {traduccion}")
            historial[frase] = traduccion
            time.sleep(5)
        elif opcion == '2':
            if historial:
                print("\nHistorial de traducciones:")
                for frase, traduccion in historial.items():
                    print(f"{frase} --> {traduccion}")
            else:
                print("No hay traducciones en el historial.")
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == '__main__':
    main()