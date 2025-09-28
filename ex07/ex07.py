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

        m2 = Matrix([
            [2, 1],
            [4, 2]
            ])

        m1.mul_mat(m2)
        m2.print_matrix()
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
