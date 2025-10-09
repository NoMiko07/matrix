from typing import Union
from vectorAndMatrixClasses import Matrix

def main():
    try:

        u = Matrix([
            [0, -5., 0.],
            [0, 3., 4.],
            [0, 1., 7.],
        ])

        """
        u = Matrix([
            [0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.],
        ])

        u = Matrix([
            [8., 5., -2., 4., 28.],
            [4., 2.5, 20., 4., -4.],
            [8., 5., 1., 4., 17.]
        ])
        """
        print(u.row_echelon())

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":  
    main()
