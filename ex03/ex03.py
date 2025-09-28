from typing import Union
from vectorAndMatrixClasses import Vector, Matrix, linear_combination, myBeartype



def main():
    try:
        v1 = Vector([-1, 6])
        v2 = Vector([3, 2])
        print(v1.dot(v2))


    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
