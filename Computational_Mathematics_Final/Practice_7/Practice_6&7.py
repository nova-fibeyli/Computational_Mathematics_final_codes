import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Задание 1: Нахождение начального ускорения с использованием данных скорости
x1 = np.array([0, 5, 10, 15, 20])  # Время (сек)
y1 = np.array([0, 3, 14, 69, 228])  # Скорость (м/с)

def newton_forward_diff(x, y):
    """Вычисление производной по формуле Ньютона (прямые разности)."""
    h = x[1] - x[0]  # Шаг (разница между соседними значениями времени)
    n = len(x)
    diff_table = np.zeros((n, n))  # Создаем таблицу конечных разностей
    diff_table[:, 0] = y  # Первый столбец заполняем значениями функции

    for j in range(1, n):  # j - уровень разности
        for i in range(n - j):  # i - индексы элементов текущего уровня
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]  # Вычисляем конечные разности

    print("Таблица конечных разностей для Задания 1:")
    print(diff_table)
    return diff_table[0][1] / h  # Возвращаем первую разность, деленную на шаг (h), что дает приближенную производную

initial_acceleration = newton_forward_diff(x1, y1)
print("Задание 1: Нахождение начального ускорения")
print(f"Начальное ускорение: {initial_acceleration:.2f} м/с^2\n")

# Визуализация для Задания 1
plt.figure(figsize=(8, 5))
plt.plot(x1, y1, 'bo-', label='Скорость (м/с)')
plt.title('Задание 1: График скорости от времени')
plt.xlabel('Время (сек)')
plt.ylabel('Скорость (м/с)')
plt.grid(True)
plt.legend()
plt.show()

# Задание 2: Найти f'(10)
x2 = np.array([3, 5, 11, 17, 27, 34])  # Массив x
y2 = np.array([-13, 23, 899, 17315, 35606, 61906])  # Массив y

def finite_diff(x, y, value):
    """Вычисление производной в указанной точке методом конечных разностей."""
    n = len(x)
    if len(y) != n:
        raise ValueError("Массивы x и y должны быть одной длины.")
    if value < x[0] or value > x[-1]:
        raise ValueError("Точка для интерполяции/экстраполяции выходит за пределы данных.")

    idx = np.searchsorted(x, value) - 1  #Индекс ближайшего меньшего элемента
    if idx < 0 or idx >= len(x) - 1:
        raise IndexError("Требуется больше данных для расчета вблизи указанной точки.")

    h = x[idx + 1] - x[idx]  # Шаг сетки
    term = (y[idx + 1] - y[idx]) / h  # Конечная разность
    return term

print("Задание 2: Нахождение производной в точке x=10")
try:
    fp_10 = finite_diff(x2, y2, 10)
    print(f"Производная в точке x=10: {fp_10:.2f}\n")
except Exception as e:
    print(f"Ошибка: {e}\n")

# Визуализация для Задания 2
plt.figure(figsize=(8, 5))
plt.plot(x2, y2, 'go-', label='Функция')
plt.title('Задание 2: График функции и касательной в точке x=10')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# Показываем касательную в точке x=10
x_tangent = np.linspace(5, 15, 100)
y_tangent = y2[1] + fp_10 * (x_tangent - x2[1])
plt.plot(x_tangent, y_tangent, 'r--', label='Касательная в x=10')
plt.legend()
plt.show()

# Задание 3: Нахождение первых трех производных
x3 = np.array([1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
y3 = np.array([3.375, 7.000, 13.625, 24.000, 38.875, 59.000])

def derivatives_at_point(x, y, point, order):
    """Нахождение производных заданного порядка."""
    n = len(x)
    diff = np.zeros((n, n))  # Таблица разностей
    diff[:, 0] = y  # Заполняем первый столбец значениями функции

    for j in range(1, n):
        for i in range(n - j):
            diff[i][j] = diff[i + 1][j - 1] - diff[i][j - 1]

    print(f"Таблица конечных разностей для точки x={point}:")
    print(diff)

    h = x[1] - x[0]  # Шаг сетки

    # Находим индекс ближайшей точки для заданного значения
    idx = np.searchsorted(x, point) - 1
    if idx < 0:
        idx = 0
    elif idx >= n - 1:
        idx = n - 2

    result = []
    for k in range(1, order + 1):
        result.append(diff[idx][k] / (h**k))  # Вычисляем производные в нужной точке
    return result


print("Задание 3: Нахождение первых трех производных")
first_second_third = derivatives_at_point(x3, y3, 1.5, 3)
print(f"Первая, вторая и третья производные: {first_second_third}\n")

# Визуализация для Задания 3
plt.figure(figsize=(8, 5))
plt.plot(x3, y3, 'mo-', label='Функция')
plt.title('Задание 3: График функции и производных')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# Показываем производные в точке x=1.5
plt.scatter(x3[0], y3[0], color='red', label='Точка x=1.5')
plt.legend()
plt.show()

# Задание 4: Первая и вторая производные в x=1.1
x4 = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
y4 = np.array([0, 0.128, 0.544, 1.296, 2.432, 4.000])

print("Задание 4: Первая и вторая производные в точке x=1.1")
derivatives_x11 = derivatives_at_point(x4, y4, 1.1, 2)
print(f"Первая и вторая производные в x=1.1: {derivatives_x11}\n")

# Визуализация для Задания 4
plt.figure(figsize=(8, 5))
plt.plot(x4, y4, 'co-', label='Функция')
plt.title('Задание 4: График функции и производных в точке x=1.1')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# Показываем производные в точке x=1.1
plt.scatter(1.1, np.interp(1.1, x4, y4), color='red', label='Точка x=1.1')
plt.legend()
plt.show()

# Задание 5: Производные для нескольких точек
x5 = np.array([1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30])
y5 = np.array([1.000, 1.025, 1.049, 1.072, 1.095, 1.118, 1.140])

print("Задание 5: Производные для нескольких точек")
for point in [1.05, 1.25, 1.15]:
    derivs = derivatives_at_point(x5, y5, point, 2)
    print(f"dy/dx и d^2y/dx^2 в точке x={point}: {derivs}")
print()

# Визуализация для Задания 5
plt.figure(figsize=(8, 5))
plt.plot(x5, y5, 'yo-', label='Функция')
plt.title('Задание 5: График функции и производных в нескольких точках')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# Показываем производные в точках 1.05, 1.15, 1.25
for point in [1.05, 1.15, 1.25]:
    plt.scatter(point, np.interp(point, x5, y5), color='red', label=f'Точка x={point}')
plt.legend()
plt.show()

# Интегрирование: Визуализация методов интегрирования
def trapezoidal_rule(f, a, b, n):
    """Правило трапеций."""
    x = np.linspace(a, b, n + 1)  # Создаем равномерную сетку
    y = f(x)  # Вычисляем значения функции
    h = (b - a) / n  # Шаг сетки
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])  # Формула трапеций

def simpsons_rule(f, a, b, n):
    """Правило Симпсона 1/3."""
    if n % 2:
        n += 1  # Увеличиваем n до ближайшего четного числа
        print(f"Количество сегментов увеличено до {n}, чтобы быть четным.")
    x = np.linspace(a, b, n + 1)  # Создаем равномерную сетку
    y = f(x)  # Вычисляем значения функции
    h = (b - a) / n  # Шаг сетки
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])  # Формула Симпсона 1/3

def simpsons_38_rule(f, a, b, n):
    """Правило Симпсона 3/8."""
    if n % 3 != 0:
        n = n + (3 - n % 3)  # Увеличиваем n до ближайшего числа, кратного 3
        print(f"Количество сегментов увеличено до {n}, чтобы быть кратным 3.")
    x = np.linspace(a, b, n + 1)  # Создаем равномерную сетку
    y = f(x)  # Вычисляем значения функции
    h = (b - a) / n  # Шаг сетки
    return (3 * h / 8) * (y[0] + 3 * np.sum(y[1:-1][::3]) + 3 * np.sum(y[2:-1][::3]) + 2 * np.sum(y[3:-1:3]) + y[-1])  # Формула Симпсона 3/8

def plot_integration(f, a, b, n, method):
    """Визуализация методов интегрирования."""
    x = np.linspace(a, b, n + 1)
    y = f(x)
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'k-', label='Функция')
    plt.title(f'Метод интегрирования: {method}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    if method == 'Правило трапеций':
        plt.fill_between(x, y, color='blue', alpha=0.3, label='Трапеции')
    elif method == 'Правило Симпсона 1/3':
        for i in range(0, n, 2):
            plt.fill_between(x[i:i+3], y[i:i+3], color='green', alpha=0.3, label='Параболы' if i == 0 else "")
    elif method == 'Правило Симпсона 3/8':
        for i in range(0, n, 3):
            plt.fill_between(x[i:i+4], y[i:i+4], color='orange', alpha=0.3, label='Кубические' if i == 0 else "")

    plt.legend()
    plt.show()

def main():
    print("Выберите метод интегрирования:")
    print("1: Правило трапеций")
    print("2: Правило Симпсона 1/3")
    print("3: Правило Симпсона 3/8")
    method = int(input("Введите номер метода (1/2/3): "))

    if method not in [1, 2, 3]:
        print("Некорректный выбор метода.")
        return

    func_input = input("Введите функцию (например, np.sin(x), np.cos(x), или x**2): ")
    f = lambda x: eval(func_input)

    try:
        a = eval(input("Введите нижний предел интегрирования a (например, 0 или np.pi): "))
        b = eval(input("Введите верхний предел интегрирования b (например, np.pi или 2): "))
        n = int(input("Введите число сегментов n: "))
    except Exception as e:
        print(f"Ошибка при вводе данных: {e}")
        return

    try:
        if method == 1:
            result = trapezoidal_rule(f, a, b, n)
            print(f"Результат (Правило трапеций): {result:.6f}")
            plot_integration(f, a, b, n, 'Правило трапеций')
        elif method == 2:
            result = simpsons_rule(f, a, b, n)
            print(f"Результат (Правило Симпсона 1/3): {result:.6f}")
            plot_integration(f, a, b, n, 'Правило Симпсона 1/3')
        elif method == 3:
            result = simpsons_38_rule(f, a, b, n)
            print(f"Результат (Правило Симпсона 3/8): {result:.6f}")
            plot_integration(f, a, b, n, 'Правило Симпсона 3/8')

        exact_integral, _ = quad(f, a, b)
        print(f"Точное значение (scipy): {exact_integral:.6f}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()# np.sqrt(np.cos(x))