def gaussian_elimination(A, B): # Вход матрица и вектор
    n = len(A) #  Возвращает количество row в матрице A

    for i in range(n):
        A[i] = [float(a) for a in A[i]]
        B[i] = float(B[i]) # Преобразует все элементы в floats

    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        B[i], B[max_row] = B[max_row], B[i] # Перестановка row

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            B[j] -= factor * B[i] # Forward elimination для приведения A к U

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = B[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i] # Обратная подстановка

    return x # Возвращает решение

def jacobi_method(A, B, iterations=25, tolerance=1e-10):
    n = len(A)
    x = [0] * n # Создаем массив нулей длины n

    for iteration in range(iterations):
        x_new = [0] * n
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (B[i] - s) / A[i][i] # Сумма всех элементов, кроме диагонали A[i][i]

        print(f"Iteration {iteration+1}: x = {x_new}")

        if max(abs(x_new[i] - x[i]) for i in range(n)) <= tolerance:
            print(f"Jacobi Method converged in {iteration+1} iterations.")
            return x_new

        x = x_new # Возвращает ответ, когда maximum change < tolerance

    return x

def gauss_seidel_method(A, B, iterations=25, tolerance=1e-10):
    n = len(A)
    x = [0] * n # Создаем массив нулей длины n

    for iteration in range(iterations):
        x_new = x[:]
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))  # Вычисляет, используя уже обновленные значения
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n)) # Вычисляет, используя старые значения
            x_new[i] = (B[i] - s1 - s2) / A[i][i]

        print(f"Iteration {iteration+1}: x = {x_new}")

        if max(abs(x_new[i] - x[i]) for i in range(n)) <= tolerance:
            print(f"Gauss-Seidel Method converged in {iteration+1} iterations.")
            return x_new

        x = x_new

    return x

def get_user_input():
    n = int(input("Enter the number of equations: "))
    A = []
    B = []
    
    print("Enter the coefficients of the equations:")
    for i in range(n):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != n:
            print("Инвалид input! Each row must have exactly", n, "coefficients.")
            return None, None
        A.append(row)

    print("Enter the right-hand side values:")
    B = list(map(float, input().split()))
    if len(B) != n:
        print("Инвалид input! The number of right-hand side values must match the number of equations.")
        return None, None
    
    return A, B

def main():
    print("Choose a method to solve the system of linear equations:")
    print("1 - Gaussian Elimination (Exact solution)")
    print("2 - Jacobi Method")
    print("3 - Gauss-Seidel Method")

    choice = input("Enter the method number: ")
    A, B = get_user_input()
    if A is None or B is None:
        print("Инвалид input! Exiting.")
        return

    if choice == "1":
        result = gaussian_elimination(A, B)
        print("Solution using Gaussian Elimination:", result)
    elif choice == "2":
        result = jacobi_method(A, B)
        print("Solution using Jacobi Method:", result)
    elif choice == "3":
        result = gauss_seidel_method(A, B)
        print("Solution using Gauss-Seidel Method:", result)
    else:
        print("Инвалид!")

if __name__ == "__main__":
    main()
