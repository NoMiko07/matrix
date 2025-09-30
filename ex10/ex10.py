from typing import Union
from vectorAndMatrixClasses import Vector, Matrix, linear_combination, myBeartype

def main():
    try:
        u = Matrix([
            [1., 0.],
            [0., 1.],
        ])
        print(u.transpose())

        u = Matrix([
            [2., -5., 0.],
            [4., 3., 7.],
            [-2., 3., 4.],
        ])
        print(u.transpose())

        u = Matrix([
            [-2., -8.],
            [1., -23.],
            [0., 6.],
        ])
        u.print_shape()
        test = u.transpose()
        test.print_matrix()

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":  
    main()
