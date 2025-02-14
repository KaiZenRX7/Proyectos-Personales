from sympy import symbols, Function, Eq, dsolve

def solve_first_order(equation, initial_value):
    x, y = symbols('x y')
    y = Function('y')(x)
    
    # Parse the equation string into a sympy equation
    eq = Eq(y.diff(x), eval(equation.replace('y', 'y(x)')))
    
    # Solve the differential equation
    solution = dsolve(eq, y)
    
    # Apply the initial condition
    C1 = symbols('C1')
    initial_condition = {y.subs(x, 0): initial_value}
    solution = solution.subs(C1, initial_condition[y])
    
    return solution

def solve_second_order(equation, initial_value, initial_derivative):
    x, y = symbols('x y')
    y = Function('y')(x)
    
    # Parse the equation string into a sympy equation
    eq = Eq(y.diff(x, x), eval(equation.replace('y', 'y(x)')))
    
    # Solve the differential equation
    solution = dsolve(eq, y)
    
    # Apply the initial conditions
    C1, C2 = symbols('C1 C2')
    initial_conditions = {y.subs(x, 0): initial_value, y.diff(x).subs(x, 0): initial_derivative}
    solution = solution.subs({C1: initial_conditions[y], C2: initial_conditions[y.diff(x)]})
    
    return solution

def evaluate_expression(expression):
    # Evaluate a mathematical expression safely
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error evaluating expression: {e}"