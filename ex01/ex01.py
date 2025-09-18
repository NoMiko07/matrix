from vectorAndMatrixClasses import Vector, Matrix , linear_combination

def main():
    try:
        v1 = Vector([1, 0, 0])
        v2 = Vector([0, 1, 0])
        v3 = Vector([0, 0, 1])
        scalar = [10, -2, 0.5]
        linear_combination([v1, v2, v3], scalar)

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
