import numpy as np

# Example Problems String
EXAMPLES_TEXT = """
Examples for Numerical Methods:

1. **Numerical Differentiation (Method 1):**
   - The following data gives the velocity of a particle for twenty seconds at an interval of five seconds.
   - Find the initial acceleration using the entire data:
     ```
     x: [0, 5, 10, 15, 20]
     y: [0, 3, 14, 69, 228]
     step size: 5
     ```

2. **Find f’(10) using Central Difference Approximation (Method 2):**
   ```
   x: [3, 5, 11, 27, 34]
   y: [-13, 23, 899, 17315, 35606]
   step size: variable depending on available data
   ```

3. **Find the first, second, and third derivatives of f(x) at x = 1.5 using Central Difference Approximation (Method 2):**
   ```
   x: [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
   y: [3.375, 7.000, 13.625, 24.000, 38.875, 59.000]
   step size: 0.5
   ```

4. **Find the first and second derivatives at x = 1.1 using Central Difference Approximation (Method 2):**
   ```
   x: [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
   y: [0, 0.128, 0.544, 1.296, 2.432, 4.00]
   step size: 0.2
   ```

5. **Find dy/dx and d²y/dx² at specific x values using Central Difference Approximation (Method 2):**
   ```
   x: [1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30]
   y: [1.000, 1.025, 1.049, 1.072, 1.095, 1.118, 1.140]
   step size: 0.05
   ```

6. **Interpolation Examples:**
- **Use Newton’s Forward Interpolation (Method 3) to estimate values:**
  ```
  Given x and y values, predict f(x) at x = x_target.
  x: [0, 5, 10, 15, 20]
  y: [0, 3, 14, 69, 228]
  x value to interpolate: 12
  ```

- **Use Lagrange Interpolation (Method 4) to estimate values:**
  ```
  Given x and y values, predict f(x) at x = x_target.
  x: [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
  y: [0, 0.128, 0.544, 1.296, 2.432, 4.00]
  x value to interpolate: 1.3
  ```
"""

def print_examples():
    """ Prints example numerical methods problems. """
    print(EXAMPLES_TEXT)

def forward_difference(x_values, y_values, step_size):
    return [(y_values[i+1] - y_values[i]) / step_size for i in range(len(y_values) - 1)]

def central_difference(x_values, y_values, step_size):
    return [(y_values[i+1] - y_values[i-1]) / (2 * step_size) for i in range(1, len(y_values) - 1)]

def newton_forward_interpolation(x_values, y_values, x_target):
    n = len(x_values)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_values
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = (diff_table[i+1][j-1] - diff_table[i][j-1]) / (x_values[i+j] - x_values[i])
    result = y_values[0]
    term = 1
    for j in range(1, n):
        term *= (x_target - x_values[j-1])
        result += term * diff_table[0][j]
    return result
def lagrange_interpolation(x_values, y_values, x_target):
    n = len(x_values)
    interpolated_value = 0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x_target - x_values[j]) / (x_values[i] - x_values[j])
        interpolated_value += term
    return interpolated_value

def get_user_input():
    x_values = list(map(float, input("Enter x values (space-separated): ").split()))
    y_values = list(map(float, input("Enter y values (space-separated): ").split()))
    return x_values, y_values

def menu():
    while True:
        print("\nNumerical Methods Program")
        print("1 - Forward Difference Approximation")
        print("2 - Central Difference Approximation")
        print("3 - Newton's Forward Interpolation")
        print("4 - Lagrange Interpolation")
        print("5 - Show Examples")
        print("6 - Exit")
        choice = input("Enter choice: ").strip()
        if choice == '6':
            print("Exiting program. Goodbye!")
            break
        if choice == '5':
            print_examples()
            continue
        x_values, y_values = get_user_input()
        if choice in ['1', '2']:
            step_size = float(input("Enter step size: "))
            result = forward_difference(x_values, y_values, step_size) if choice == '1' else central_difference(x_values, y_values, step_size)
            print("Result:", result)
if __name__ == "__main__":
    menu()