from typing import Union
from vectorAndMatrixClasses import Matrix

def main():
    try:
        
        u = Matrix([
            [1., 0., 0.],
            [0., 1., 0.],
            [0., 0., 1.],
        ])
        print(u.inverse(), "\n")

        u = Matrix([
            [2., 0., 0.],
            [0., 2., 0.],
            [0., 0., 2.],
        ])
        print(u.inverse(), "\n")

        u = Matrix([
            [8., 5., -2.],
            [4., 7., 20.],
            [7., 6., 1.],
        ])
        print(u.inverse(), "\n")
        
        u = Matrix([
            [0., 3., 0.],
            [3., 0., 0.],
            [0., 0., 3.],
        ])
        print(u.inverse())
        

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":  
    main()
