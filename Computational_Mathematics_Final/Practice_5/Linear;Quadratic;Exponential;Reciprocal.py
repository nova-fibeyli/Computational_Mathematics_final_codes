import math
import matplotlib.pyplot as plt

# Utility functions
def calculate_rmsl(y_observed, y_predicted):
    total = 0
    count = len(y_observed)
    for i in range(count):
        diff = y_observed[i] - y_predicted[i]
        total += diff * diff
    return (total / count) ** 0.5

# Model functions
def linear_model(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum(xi * xi for xi in x)
    sum_xy = sum(x[i] * y[i] for i in range(n))

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
    b = (sum_y - a * sum_x) / n
    return a, b

def quadratic_model(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(xi * xi for xi in x)
    sum_x3 = sum(xi ** 3 for xi in x)
    sum_x4 = sum(xi ** 4 for xi in x)
    sum_y = sum(y)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    sum_x2y = sum(x[i] ** 2 * y[i] for i in range(n))

    matrix = [
        [n, sum_x, sum_x2, sum_y],
        [sum_x, sum_x2, sum_x3, sum_xy],
        [sum_x2, sum_x3, sum_x4, sum_x2y]
    ]

    for i in range(3):
        for j in range(i + 1, 3):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(4):
                matrix[j][k] -= ratio * matrix[i][k]

    c = matrix[2][3] / matrix[2][2]
    b = (matrix[1][3] - matrix[1][2] * c) / matrix[1][1]
    a = (matrix[0][3] - matrix[0][1] * b - matrix[0][2] * c) / matrix[0][0]
    return a, b, c

def exponential_model(x, y):
    log_y = [math.log(yi) if yi > 0 else 0 for yi in y]
    a, b = linear_model(x, log_y)
    return math.exp(a), b

def reciprocal_model(x, y):
    new_x = [1 / xi if xi != 0 else 0 for xi in x]
    return linear_model(new_x, y)

# Plotting function
def plot_model(x, y, x_label, y_label, title, coeffs, label_format, model, initial_guess=None):
    plt.scatter(x, y, color="blue", label="Observed Data")

    x_fit = sorted(x)
    y_fit = []
    for xi in x_fit:
        if model == "linear":
            y_fit.append(coeffs[0] * xi + coeffs[1])
        elif model == "quadratic":
            y_fit.append(coeffs[0] * xi ** 2 + coeffs[1] * xi + coeffs[2])
        elif model == "exponential":
            y_fit.append(coeffs[0] * math.exp(coeffs[1] * xi))
        elif model == "reciprocal":
            y_fit.append(coeffs[0] * xi + coeffs[1] / xi)

    plt.plot(x_fit, y_fit, color="red", label="Fitted Curve")
    
    # Plot initial guess if provided
    if initial_guess:
        y_initial_guess = []
        for xi in x_fit:
            if model == "linear":
                y_initial_guess.append(initial_guess[0] * xi + initial_guess[1])
            elif model == "quadratic":
                y_initial_guess.append(initial_guess[0] * xi ** 2 + initial_guess[1] * xi + initial_guess[2])
            elif model == "exponential":
                y_initial_guess.append(initial_guess[0] * math.exp(initial_guess[1] * xi))
            elif model == "reciprocal":
                y_initial_guess.append(initial_guess[0] * xi + initial_guess[1] / xi)
        plt.plot(x_fit, y_initial_guess, color="green", linestyle="--", label="Initial Guess")

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

# Function to detect model type from equation
def detect_model(equation):
    equation = equation.replace(" ", "")  # Remove spaces

    if "^2" in equation or "x**2" in equation:
        return "quadratic"
    elif "e^" in equation or "exp(" in equation:
        return "exponential"
    elif "/x" in equation or "1/x" in equation:
        return "reciprocal"
    elif "x" in equation:
        return "linear"
    else:
        raise ValueError("Unrecognized equation format. Supported formats are linear, quadratic, exponential, or reciprocal.")

# Example Solutions
def example_solutions():
    examples = {
        1: {
            "x": [0, 1, 2, 3, 4],
            "y": [1, 1.8, 1.3, 2, 6.3],
            "model": "quadratic",
            "equation": "y = ax^2 + bx + c",
            "initial_guess": [1, 0, 0]  # Initial guess for a, b, c
        },
        2: {
            "x": [6, 7, 7, 8, 8, 8, 9, 9, 10],
            "y": [5, 5, 4, 5, 4, 3, 4, 3, 3],
            "model": "linear",
            "equation": "y = ax + b",
            "initial_guess": [0, 1]  # Initial guess for a, b
        },
        3: {
            "x": [0, 1, 2, 3],
            "y": [1.05, 2.10, 3.85, 8.30],
            "model": "exponential",
            "equation": "y = ae^(bx)",
            "initial_guess": [1, 0.5]  # Initial guess for a, b
        },
        4: {
            "x": [1, 2, 3, 4, 5],
            "y": [1.8, 5.1, 8.9, 14.1, 19.8],
            "model": "quadratic",
            "equation": "y = ax^2 + bx + c",
            "initial_guess": [1, 1, 0]  # Initial guess for a, b, c
        },
        5: {
            "x": [1, 2, 3, 4, 5, 6, 7, 8],
            "y": [5.4, 6.3, 8.2, 10.3, 12.6, 14.9, 17.3, 19.5],
            "model": "reciprocal",
            "equation": "y = ax + b/x",
            "initial_guess": [1, 1]  # Initial guess for a, b
        }
    }

    print("\nExample Solutions:")
    for key, value in examples.items():
        print(f"{key}. {value['equation']} (Model: {value['model']})")

    choice = int(input("Select an example number: "))
    if choice in examples:
        example = examples[choice]
        x = example["x"]
        y = example["y"]
        model_type = example["model"]
        initial_guess = example["initial_guess"]

        if model_type == "linear":
            coeffs = linear_model(x, y)
            label_format = "y = {0:.2f}x + {1:.2f}"
        elif model_type == "quadratic":
            coeffs = quadratic_model(x, y)
            label_format = "y = {0:.2f}x^2 + {1:.2f}x + {2:.2f}"
        elif model_type == "exponential":
            coeffs = exponential_model(x, y)
            label_format = "y = {0:.2f}e^({1:.2f}x)"
        elif model_type == "reciprocal":
            coeffs = reciprocal_model(x, y)
            label_format = "y = {0:.2f}x + {1:.2f}/x"
        else:
            print("Unrecognized model type.")
            return

        predicted_y = []
        for xi in x:
            if model_type == "linear":
                predicted_y.append(coeffs[0] * xi + coeffs[1])
            elif model_type == "quadratic":
                predicted_y.append(coeffs[0] * xi ** 2 + coeffs[1] * xi + coeffs[2])
            elif model_type == "exponential":
                predicted_y.append(coeffs[0] * math.exp(coeffs[1] * xi))
            elif model_type == "reciprocal":
                predicted_y.append(coeffs[0] * xi + coeffs[1] / xi)

        rmsl = calculate_rmsl(y, predicted_y)
        print(f"Initial Guess: {initial_guess}")
        print(f"Coefficients: {coeffs}")
        print(f"RMSL: {rmsl:.2f}")
        plot_model(x, y, "X", "Y", "Example Solution", coeffs, label_format, model_type, initial_guess)
    else:
        print("Invalid choice.")

# Menu System
def menu():
    while True:
        print("\nMenu:")
        print("1. Solve an example solution")
        print("2. Input custom x and y values")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            example_solutions()
        elif choice == "2":
            x_values = list(map(float, input("Enter x values (space-separated): ").split()))
            y_values = list(map(float, input("Enter y values (space-separated): ").split()))

            if len(x_values) != len(y_values):
                print("Error: x and y values must have the same length.")
                continue

            equation = input("Enter the equation (e.g., 'y = ax + b', 'y = ax^2 + bx + c', etc.): ").strip()
            try:
                model_type = detect_model(equation)
            except ValueError as e:
                print(e)
                continue

            if model_type == "linear":
                coeffs = linear_model(x_values, y_values)
                label_format = "y = {0:.2f}x + {1:.2f}"
            elif model_type == "quadratic":
                coeffs = quadratic_model(x_values, y_values)
                label_format = "y = {0:.2f}x^2 + {1:.2f}x + {2:.2f}"
            elif model_type == "exponential":
                coeffs = exponential_model(x_values, y_values)
                label_format = "y = {0:.2f}e^({1:.2f}x)"
            elif model_type == "reciprocal":
                coeffs = reciprocal_model(x_values, y_values)
                label_format = "y = {0:.2f}x + {1:.2f}/x"
            else:
                print("Unrecognized model type.")
                continue

            predicted_y = []
            for xi in x_values:
                if model_type == "linear":
                    predicted_y.append(coeffs[0] * xi + coeffs[1])
                elif model_type == "quadratic":
                    predicted_y.append(coeffs[0] * xi ** 2 + coeffs[1] * xi + coeffs[2])
                elif model_type == "exponential":
                    predicted_y.append(coeffs[0] * math.exp(coeffs[1] * xi))
                elif model_type == "reciprocal":
                    predicted_y.append(coeffs[0] * xi + coeffs[1] / xi)

            rmsl = calculate_rmsl(y_values, predicted_y)
            print(f"Coefficients: {coeffs}")
            print(f"RMSL: {rmsl:.2f}")
            plot_model(x_values, y_values, "X", "Y", "Custom Input Solution", coeffs, label_format, model_type)

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
