from typing import Union
from vectorAndMatrixClasses import Vector, Matrix, linear_combination, myBeartype

Number = Union[int, float]

def impl(u: "Vector", v: "Vector") -> Number:
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise ValueError("u and v must be vectors.")
    if u.size() != v.size():
        raise ValueError("u and v must have the same length.")

    scalar = 0
    for x, y in zip(u.values, v.values):
        scalar = (scalar + x * y)
    return scalar

def main():
    try:
        v1 = Vector([-1, 6])
        v2 = Vector([3, 2])
        print(impl(v1, v2))


    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
