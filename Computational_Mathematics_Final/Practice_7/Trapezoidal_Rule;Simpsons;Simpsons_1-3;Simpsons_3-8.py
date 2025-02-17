import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])

def simpsons_rule(f, a, b, n):
    if n % 2:
        n += 1
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

def simpsons_one_third_rule(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 3) * (y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2]) + y[-1])

def simpsons_three_eighths_rule(f, a, b, n):
    if n % 3 != 0:
        n += 3 - (n % 3)
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (3 * h / 8) * (y[0] + 3 * sum(y[1:-1:3]) + 3 * sum(y[2:-1:3]) + 2 * sum(y[3:-1:3]) + y[-1])

def visualize_function(f, a, b):
    x = np.linspace(a, b, 100)
    y = f(x)
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'b-', label='Function')
    plt.title('Function Visualization')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    print("Choose a method:")
    print("1: Trapezoidal Rule")
    print("2: Simpson's Rule")
    print("3: Simpson's 1/3 Rule")
    print("4: Simpson's 3/8 Rule")

    choice = int(input("Enter the method number (1-4): "))

    f_str = input("Enter the function of x (e.g., 'x**3', 'np.sin(x)', 'np.log10(x)', 'np.exp(x)', ctg - '1 / np.tan(x)' or 'np.sqrt(x)'): ")
    f = lambda x: eval(f_str)

    a = eval(input("Enter the lower limit of integration (a) (e.g., 'np.pi / 4' or '1'): "))
    b = eval(input("Enter the upper limit of integration (b (e.g., 'np.pi' or '2')): "))
    n = int(input("Enter the number of intervals (n (e.g., 10)): "))

    if choice == 1:
        result = trapezoidal_rule(f, a, b, n)
        print(f"Trapezoidal Rule Result: {result:.6f}")
    elif choice == 2:
        result = simpsons_rule(f, a, b, n)
        print(f"Simpson's Rule Result: {result:.6f}")
    elif choice == 3:
        result = simpsons_one_third_rule(f, a, b, n)
        print(f"Simpson's 1/3 Rule Result: {result:.6f}")
    elif choice == 4:
        result = simpsons_three_eighths_rule(f, a, b, n)
        print(f"Simpson's 3/8 Rule Result: {result:.6f}")
    else:
        print("Invalid choice. Please select a number from 1 to 4.")
        return

    visualize_function(f, a, b)

if __name__ == "__main__":
    main()
