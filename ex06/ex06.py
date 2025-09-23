from typing import Union
from vectorAndMatrixClasses import Vector, Matrix, linear_combination, myBeartype

def cross_product(u: "Vector", v: "Vector") -> "Vector":
    """
    u * v = (u2 * v3 - u3 * v2, u3 * v1 - u1 * v3, u1 * v2 - u2 * v1)
    """
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise ValueError("u and v must be vectors.")
    if u.size() != 3 and  v.size() != 3:
        raise ValueError("u and v must be a 3d vector.")
    
    newVector = []
    u1 = u.values[0]
    u2 = u.values[1]
    u3 = u.values[2]    
    v1 = v.values[0]
    v2 = v.values[1]
    v3 = v.values[2]
    
    newVector.append(u2 * v3 - u3 * v2)
    newVector.append(u3 * v1 - u1 * v3)
    newVector.append(u1 * v2 - u2 * v1)

    return Vector(newVector)
    
def main():
    try:
        v1 = Vector([0., 0., 1.])
        v2 = Vector([1., 0., 0.])
        print(cross_product(v1, v2))

        v1 = Vector([1., 2., 3.])
        v2 = Vector([4., 5., 6.])
        print(cross_product(v1, v2))

        v1 = Vector([4., 2., -3.])
        v2 = Vector([-2., -5., 16.])
        print(cross_product(v1, v2))

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
