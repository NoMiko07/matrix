from typing import Union
from vectorAndMatrixClasses import Matrix

def main():
    try:
        u = Matrix([
            [ 0., 1.],
            [1., 0.],
        ])
        print(u.determinant())

        u = Matrix([
            [ 1., -1.],
            [-1., 1.],
        ])
        print(u.determinant())

        u = Matrix([
            [2., 0., 0.],
            [0., 2., 0.],
            [0., 0., 2.],
        ])
        print(u.determinant())
        
        u = Matrix([
            [8., 5., -2.],
            [4., 7., 20.],
            [7., 6., 1.],
        ])
        print(u.determinant())
        u = Matrix([
            [ 8., 5., -2., 4.],
            [ 4., 2.5, 20., 4.],
            [ 8., 5., 1., 4.],
            [28., -4., 17., 1.],
        ])
        print(u.determinant())

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":  
    main()
