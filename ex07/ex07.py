from typing import Union
from vectorAndMatrixClasses import Vector, Matrix, linear_combination, myBeartype


def main():
    try:
        u = Matrix([
            [1., 0.],
            [0., 1.],
        ])
        v = Vector([4., 2.])
        print(u.mul_vec(v))

        u = Matrix([
            [2., 0.],
            [0., 2.],
        ])
        v = Vector([4., 2.])
        print(u.mul_vec(v))

        u = Matrix([
            [2., -2.],
            [-2., 2.],
        ])
        v = Vector([4., 2.])
        print(u.mul_vec(v))

        u = Matrix([
            [1., 0.],
            [0., 1.],
        ])
        v = Matrix([
            [1., 0.],
            [0., 1.],
        ])
        print(u.mul_mat(v))

        u = Matrix([
            [1., 0.],
            [0., 1.],
        ])
        v = Matrix([
            [2., 1.],
            [4., 2.],
        ])
        print(u.mul_mat(v))

        u = Matrix([
            [3., -5.],
            [6., 8.],
        ])
        v = Matrix([
            [2., 1.],
            [4., 2.],
        ])
        print(u.mul_mat(v))
        

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":  
    main()
