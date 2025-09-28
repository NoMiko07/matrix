from typing import Union
from vectorAndMatrixClasses import Vector, Matrix, linear_combination, myBeartype


    
def main():
    try:
        v1 = Vector([4, 2])
        m1 = Matrix([
            [3., -5.],
            [6., 8.],
            ])
        #print(m1.mul_vec(v1))

        m1 = Matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            ])
        
        m2 = Matrix([
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1],
            ])

        print(m1.mul_mat(m2))
        

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":  
    main()
