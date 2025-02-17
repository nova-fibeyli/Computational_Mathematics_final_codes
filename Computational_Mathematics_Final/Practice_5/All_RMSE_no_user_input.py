import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = np.array([0, 1, 2, 3, 4]) #ollama run llama3.2
y = np.array([1, 1.8, 1.3, 2, 6.3])

# 1) y = a + bx + cx^2 (Quadratic polynomial)
coeff_parabola = np.polyfit(x, y, 2)
y_parabola_fit = np.polyval(coeff_parabola, x)

# 2) y = a + bx (Linear polynomial)
coeff_line = np.polyfit(x, y, 1)
y_line_fit = np.polyval(coeff_line, x)

# 3) y = ae^(bx) (Exponential function)
def exp_func(x, a, b):
    return a * np.exp(b * x)

params_exp, _ = curve_fit(exp_func, x, y, p0=[1, 0.1])
y_exp_fit = exp_func(x, *params_exp)


# 4) y = a + bx + cx^2 + dx^3 (Cubic polynomiaд)
coeff_cubic = np.polyfit(x, y, 3)
y_cubic_fit = np.polyval(coeff_cubic, x)

# 5) y = ax + b/x
def rational_func(x, a, b):
    return a * x + b / x

# Handle non-zero x values
try:
    x_non_zero = x[x != 0]
    y_non_zero = y[x != 0]
    params_rational, _ = curve_fit(rational_func, x_non_zero, y_non_zero)
    y_rational_fit = np.zeros_like(x, dtype=float)
    non_zero_indices = x != 0
    y_rational_fit[non_zero_indices] = rational_func(x[non_zero_indices], *params_rational)
except Exception as e:
    print("Error in fitting the rational function:", e)
    y_rational_fit = np.full_like(x, np.nan)

def mse(y_true, y_fit):
    return np.mean((y_true - y_fit)**2)

def rmse(y_true, y_fit):
    return np.sqrt(mse(y_true, y_fit))

rmse_parabola = rmse(y, y_parabola_fit)
rmse_line = rmse(y, y_line_fit)
rmse_exp = rmse(y, y_exp_fit)
rmse_cubic = rmse(y, y_cubic_fit)
rmse_rational = rmse(y, y_rational_fit)

print(f"RMSE for Parabola: {rmse_parabola:.4f}")
print(f"RMSE for Line: {rmse_line:.4f}")
print(f"RMSE for Exponential Curve: {rmse_exp:.4f}")
print(f"RMSE for Cubic Polynomial: {rmse_cubic:.4f}")
print(f"RMSE for Rational Curve: {rmse_rational:.4f}")

rmse_values = [rmse_parabola, rmse_line, rmse_exp, rmse_cubic, rmse_rational]
best_model_index = np.argmin(rmse_values)

model_names = ["Parabola", "Line", "Exponential", "Cubic", "Rational"]
best_model_name = model_names[best_model_index]
best_rmse_value = rmse_values[best_model_index]

print(f"Best RMSE ({best_model_name}): {best_rmse_value:.4f}")
if best_model_index == 0:  # Parabola
    label = f'Parabola: y = {coeff_parabola[0]:.4f}x^2 + {coeff_parabola[1]:.4f}x + {coeff_parabola[2]:.4f}'
elif best_model_index == 1:  # Line
    label = f'Line: y = {coeff_line[0]:.4f}x + {coeff_line[1]:.4f}'
elif best_model_index == 2:  # Exponential
    label = f'Exp: y = {params_exp[0]:.4f}e^({params_exp[1]:.4f}x)'
elif best_model_index == 3:  # Cubic Polynomial
    label = f'Cubic: y = {coeff_cubic[0]:.4f}x^3 + {coeff_cubic[1]:.4f}x^2 + {coeff_cubic[2]:.4f}x + {coeff_cubic[3]:.4f}'
else:  # Rational
    label = f'Rational: y = {params_rational[0]:.4f}x + {params_rational[1]:.4f}/x'

x_fit = np.linspace(min(x), max(x), 100)
if best_model_index == 0:  # Parabola
    y_best_fit = np.polyval(coeff_parabola, x_fit)
elif best_model_index == 1:  # Line
    y_best_fit = np.polyval(coeff_line, x_fit)
elif best_model_index == 2:  # Exponential
    y_best_fit = exp_func(x_fit, *params_exp)
elif best_model_index == 3:  # Cubic Polynomial
    y_best_fit = np.polyval(coeff_cubic, x_fit)
else:  # Rational
    y_best_fit = rational_func(x_fit, *params_rational)

plt.scatter(x, y, color='red', label='Original data')
plt.plot(x_fit, y_best_fit, label=label, color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Best Fit Curve (with RMSE)')
plt.show()
