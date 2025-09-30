from typing import Union
from vectorAndMatrixClasses import Vector, Matrix, linear_combination, myBeartype

def main():
    try:
        u = Matrix([
            [1., 0.],
            [0., 1.],
        ])
        print(u.trace())

        u = Matrix([
            [2., -5., 0.],
            [4., 3., 7.],
            [-2., 3., 4.],
        ])
        print(u.trace())

        u = Matrix([
            [-2., -8., 4.],
            [1., -23., 4.],
            [0., 6., 4.],
        ])
        print(u.trace())

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":  
    main()
