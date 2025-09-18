from vectorAndMatrixClasses import Vector, Matrix 

def main():
    try:
        # === TEST VECTEURS ===
        print("=== Vector Tests ===")
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])

        # Addition
        v1.add(v2)
        v1.print_vector()

        # Soustraction
        v1.sub(v2)
        v1.print_vector()

        # Multiplication par un scalaire
        v1.scl(10)
        v1.print_vector()

        # === TEST MATRICES ===
        print("\n=== Matrix Tests ===")
        m1 = Matrix([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix([[1, 2, 3], [4, 5, 6]])

        # Addition
        m1.add(m2)
        print("After m1.add(m2):")
        m1.print_matrix()

        # Soustraction
        m1.sub(m2)
        print("After m1.sub(m2):")
        m1.print_matrix()

        # Multiplication par un scalaire
        m1.scl(10)
        print("After m1.scl(10):")
        m1.print_matrix()

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
