import math
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Function parsing with sympy
def parse_function(expression):
    """
    Converts a user-input mathematical expression into a callable function.
    """
    x = sp.symbols('x')
    try:
        return sp.lambdify(x, sp.sympify(expression), 'math')
    except Exception as e:
        print("\nInvalid function format:", e)
        exit()

def derivative(expression):
    """
    Computes the derivative of the given function as a sympy expression.
    """
    x = sp.symbols('x')
    try:
        func_expr = sp.sympify(expression)
        d_func_expr = sp.diff(func_expr, x)
        return sp.lambdify(x, d_func_expr, 'math')
    except Exception as e:
        print("\nError computing derivative:", e)
        exit()

def bisection_method(func, a, b, epsilon):
    """
    Finds the root of a function using the Bisection Method.
    """
    if func(a) * func(b) >= 0:
        print("\nError: Function does not change sign in the interval. Try another interval.")
        return None

    iteration = 1
    while (b - a) / 2 > epsilon:
        x = (a + b) / 2
        print(f"{iteration}-iteration: x = {x:.6f}, f(x) = {func(x):.6f}")

        if abs(func(x)) < epsilon or (b - a) < epsilon:
            return x

        if func(x) * func(a) < 0:
            b = x
        else:
            a = x

        iteration += 1

    return x

def newton_raphson_method(expression, x0, epsilon, max_iter=50):
    """
    Uses Newton-Raphson method to find roots.
    """
    func = parse_function(expression)
    d_func = derivative(expression)

    iteration = 1
    while iteration <= max_iter:
        if abs(d_func(x0)) < 1e-10:
            print("\nError: Derivative is too small. Newton-Raphson method may not converge.")
            return None
        
        x1 = x0 - func(x0) / d_func(x0)
        print(f"{iteration}-iteration: x = {x1:.6f}, f(x) = {func(x1):.6f}")

        if abs(x1 - x0) < epsilon:
            return x1

        x0 = x1
        iteration += 1

    print("\nWarning: Newton-Raphson method did not converge within max iterations.")
    return None

def false_position_method(func, a, b, epsilon, max_iter=50):
    """
    Uses the False Position (Regula Falsi) method to find roots.
    """
    if func(a) * func(b) >= 0:
        print("\nError: Function does not change sign in the interval. Try another interval.")
        return None

    iteration = 1
    while iteration <= max_iter:
        x = (a * func(b) - b * func(a)) / (func(b) - func(a))  # False Position formula
        print(f"{iteration}-iteration: x = {x:.6f}, f(x) = {func(x):.6f}")

        if abs(func(x)) < epsilon:
            return x

        if func(x) * func(a) < 0:
            b = x
        else:
            a = x

        iteration += 1

    print("\nWarning: False Position method did not converge within max iterations.")
    return None

def fixed_point_iteration_method(func, g_func, x0, epsilon, max_iter=50):
    """
    Uses Fixed-Point Iteration method to find roots.
    """
    iteration = 1
    while iteration <= max_iter:
        x1 = g_func(x0)
        print(f"{iteration}-iteration: x = {x1:.6f}, f(x) = {func(x1):.6f}")

        if abs(x1 - x0) < epsilon:
            return x1

        x0 = x1
        iteration += 1

    print("\nWarning: Fixed-Point Iteration method did not converge within max iterations.")
    return None

def main():
    """
    Main user interface to choose mathematical operations.
    """
    x = sp.symbols('x')
    
    print("\nChoose an operation:")
    print("1 - Find Root of a Function")
    print("2 - Compute Definite Integral")
    print("3 - Compute Discriminant of Quadratic Equation")
    choice = input("Enter choice (1, 2, or 3): ").strip()

    expression = input("\nEnter a function (use 'x' as variable, e.g., 'x**2 - 4' or 'cos(x) - x'): ").strip()

    if choice == "1":
        print("\nChoose a method:")
        print("1 - Bisection Method (Requires Interval [a, b])")
        print("2 - Newton-Raphson Method (Requires Initial Guess x0)")
        print("3 - False Position Method (Requires Interval [a, b])")
        print("4 - Fixed-Point Iteration Method (Requires Initial Guess x0 & g(x))")
        method_choice = input("Enter method choice (1, 2, 3, or 4): ").strip()

        epsilon = float(input("Enter precision (epsilon): "))

        if method_choice in ["1", "3"]:  # Bisection or False Position
            a = float(input("Enter interval start (a): "))
            b = float(input("Enter interval end (b): "))
            func = parse_function(expression)

            if method_choice == "1":
                print("\nBisection Method:")
                root = bisection_method(func, a, b, epsilon)
                method_name = "Bisection"

            else:  # method_choice == "3"
                print("\nFalse Position Method:")
                root = false_position_method(func, a, b, epsilon)
                method_name = "False Position"

        elif method_choice in ["2", "4"]:  # Newton-Raphson or Fixed-Point Iteration
            x0 = float(input("Enter initial guess x0: "))
            func = parse_function(expression)

            if method_choice == "2":
                print("\nNewton-Raphson Method:")
                root = newton_raphson_method(expression, x0, epsilon)
                method_name = "Newton-Raphson"

            else:  # method_choice == "4"
                g_expression = input("Enter g(x) for Fixed-Point Iteration (e.g., 'sqrt(2 + x)'): ").strip()
                g_func = parse_function(g_expression)
                print("\nFixed-Point Iteration Method:")
                root = fixed_point_iteration_method(func, g_func, x0, epsilon)
                method_name = "Fixed-Point Iteration"

        else:
            print("\nInvalid method choice. Exiting.")
            return

        if root is not None:
            print(f" Root found at x = {root:.6f} using {method_name} Method.")

    else:
        print("\nInvalid choice. Exiting.")

    print("\n# Operation Completed Successfully!")

if __name__ == "__main__":
    main()
