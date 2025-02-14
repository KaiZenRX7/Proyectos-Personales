def main():
    print("¡Bienvenido a la Calculadora de Funciones y Ecuaciones Diferenciales!")
    print("Seleccione una opción:")
    print("1. Operaciones Básicas")
    print("2. Resolver Ecuaciones Diferenciales")
    
    choice = input("Ingrese su elección (1 o 2): ")
    
    if choice == '1':
        handle_basic_operations()
    elif choice == '2':
        handle_differential_equations()
    else:
        print("Elección inválida. Por favor seleccione 1 o 2.")

def handle_basic_operations():
    from calculator import Calculator
    calc = Calculator()
    
    print("Operaciones Básicas:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    operation = input("Seleccione una operación (1-4): ")
    try :
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Por favor ingrese números válidos.")
        return
    if operation == '1':
        result = calc.add(num1, num2)
    elif operation == '2':
        result = calc.subtract(num1, num2)
    elif operation == '3':
        result = calc.multiply(num1, num2)
    elif operation == '4':
        result = calc.divide(num1, num2)
    else:
        print("Operación inválida.")
        return
    
    print(f"El resultado es: {result}")

def handle_differential_equations():
    from utils.differential_equations import solve_first_order, solve_second_order
    
    print("Ecuaciones Diferenciales:")
    print("1. Resolver de Primer Orden")
    print("2. Resolver de Segundo Orden")
    
    eq_choice = input("Seleccione un tipo de ecuación (1 o 2): ")
    
    if eq_choice == '1':
        print("Seleccione una ecuación diferencial de primer orden:")
        equations = [
            "dy/dx = y + x",
            "dy/dx = y - x",
            "dy/dx = y * x",
            "dy/dx = y / x"
        ]
        for i, eq in enumerate(equations, 1):
            print(f"{i}. {eq}")
        eq_index = int(input("Ingrese el número de la ecuación: ")) - 1
        if 0 <= eq_index < len(equations):
            equation = equations[eq_index]
            initial_value = float(input("Ingrese el valor inicial (y0): "))
            result = solve_first_order(equation, initial_value)
        else:
            print("Selección inválida.")
            return
    elif eq_choice == '2':
        print("Seleccione una ecuación diferencial de segundo orden:")
        equations = [
            "d2y/dx2 = y + x",
            "d2y/dx2 = y - x",
            "d2y/dx2 = y * x",
            "d2y/dx2 = y / x"
        ]
        for i, eq in enumerate(equations, 1):
            print(f"{i}. {eq}")
        eq_index = int(input("Ingrese el número de la ecuación: ")) - 1
        if 0 <= eq_index < len(equations):
            equation = equations[eq_index]
            initial_value = float(input("Ingrese el valor inicial (y0): "))
            initial_derivative = float(input("Ingrese el valor inicial de la derivada (dy0/dx): "))
            result = solve_second_order(equation, initial_value, initial_derivative)
        else:
            print("Selección inválida.")
            return
    else:
        print("Elección inválida.")
        return
    
    print(f"La solución es: {result}")

if __name__ == "__main__":
    main()