from vectorAndMatrixClasses import Vector, Matrix, linear_combination, myBeartype


def main():
    try:
        v1 = Vector([0, 0, 0])
        print(f"{v1.norm_1()}, {v1.norm()}, {v1.norm_inf()}")
        v1 = Vector([1, 2, 3])
        print(f"{v1.norm_1()}, {v1.norm()}, {v1.norm_inf()}")
        v1 = Vector([-1, -2])
        print(f"{v1.norm_1()}, {v1.norm()}, {v1.norm_inf()}")


    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
