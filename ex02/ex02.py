from vectorAndMatrixClasses import Vector, Matrix ,linear_combination, myBeartype
from typing import Union

Number = Union[int, float]

def lerp_Scalar(u: Number, v: Number, t: Number):
    return (1 - t) * u + t * v


def lerp_Vector(v1: "Vector", v2: "Vector", t: Number):
    print(v1.size(), v2.size())
    if v1.size() != v2.size():
        raise ValueError("Vectors must have the same lenght.")
    
    newVector = []
    for u, v in zip(v1.values, v2.values):
        newVector.append(round((1 - t) * u + t * v, 1))
    
    return Vector(newVector)


    
    
def lerp_Matrix(m1: "Matrix", m2: "Matrix", t: Number):
    if m1.shape() != m2.shape():
        raise ValueError("Vectors must have the same lenght.")
    
    newMatrix = []
    for row1, row2 in zip(m1.rows, m2.rows):
        newVector = []
        for u, v in zip(row1, row2):
            newVector.append(round((1 - t) * u + t * v, 1))
        newMatrix.append(newVector)
    return Matrix(newMatrix)


def lerp(u, v, t) -> any:
    if t < 0 or t > 1:
        raise ValueError("t must be between 0 to 1.")
    
    if isinstance(u, Number) and isinstance(v, Number):
        u = float(u)
        v = float(v)

    if not isinstance(u, type(v)):
        raise ValueError("u and v must have the same type.")
    
    if t == 1:
        return v
    elif t == 0:
        return u
    
    if isinstance(u, Number):
        return lerp_Scalar(u, v, t)
    elif isinstance(u, Vector):
        return lerp_Vector(u, v, t)
    elif isinstance(u, Matrix):
        return lerp_Matrix(u, v, t)
    else:
        raise ValueError("lerp can only handle , int/float/Vector/Matrix")
def main():
    try:
        v1 = Vector([2, 1])
        v2 = Vector([4, 2])
        m1 = Matrix([[2., 1.], [3., 4.]])
        m2 = Matrix([[20.,10.], [30., 40.]])

        print(lerp(m1, m2 , 0.5))
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
