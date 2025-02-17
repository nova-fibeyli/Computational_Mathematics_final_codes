import numpy as np

def compute_matrix_decomposition(matrix):
    """
    If matrix is square or not.
    If square, computes Eigenvalues & Eigenvectors.
    If not, performs Singular Value Decomposition (SVD).
    """
    matrix = np.array(matrix)
    rows, cols = matrix.shape

    if rows == cols:  # If matrix is square, compute eigenvalues & eigenvectors
        print("\nMatrix is square, computing eigenvalues and eigenvectors...")
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        print("\nEigenvalues:", eigenvalues)
        print("\nEigenvectors:\n", eigenvectors)
    else:
        print("\nMatrix is not square, performing Singular Value Decomposition (SVD)...")
        U, S, Vt = np.linalg.svd(matrix)
        print("\nU (Left Singular Vectors):\n", U)
        print("\nSingular Values:\n", S)
        print("\nV^T (Right Singular Vectors Transposed):\n", Vt)

def compute_matrix_inverse(matrix):
    """
    Computes the inverse of a square matrix if it is invertible.
    """
    matrix = np.array(matrix)
    rows, cols = matrix.shape

    if rows == cols:
        try:
            inverse = np.linalg.inv(matrix)
            print("\nInverse Matrix:\n", inverse)
        except np.linalg.LinAlgError:
            print("\nMatrix is singular and cannot be inverted.")
    else:
        print("\nMatrix is not square, cannot compute inverse.")

def get_user_matrix():
    """
    Waits for matrix row by row.
    Transforms input into a 2D list.
    """
    print("\nProvide your matrix row by row, separating numbers with spaces.")
    print("Example input for a 3x3 matrix:\n 6 1 1\n 4 -2 5\n 2 8 7")
    print("\nTo finish input, press Enter after the last row.")

    rows = []
    while True:
        row = input("Enter row (or press Enter to finish): ").strip()
        if row == "":
            break
        try:
            row_data = list(map(float, row.split()))
            if len(rows) > 0 and len(row_data) != len(rows[0]):
                print("Invalid input! All rows must have the same number of columns.")
                continue
            rows.append(row_data)
        except ValueError:
            print("Invalid input! Please enter numeric values separated by spaces.")

    if len(rows) == 0:
        print("No valid matrix entered. Exiting program.")
        exit()

    return np.array(rows)

def main():
    print("\nChoose an operation:")
    print("1 - Compute Eigenvalues & Eigenvectors or SVD")
    print("2 - Compute Inverse of the Matrix")
    choice = input("Enter choice (1 or 2): ").strip()

    user_matrix = get_user_matrix()

    if choice == "1":
        compute_matrix_decomposition(user_matrix)
    elif choice == "2":
        compute_matrix_inverse(user_matrix)
    else:
        print("Invalid. Exiting.")

    print("\n# Operation Completed Successfully!")

if __name__ == "__main__":
    main()
