try:
    # Código que puede lanzar una excepción
    resultado = 10 / 0
except ZeroDivisionError as e:
    # Captura la excepción y la almacena en la variable 'e'
    print(f"Ocurrió un error: {e}")