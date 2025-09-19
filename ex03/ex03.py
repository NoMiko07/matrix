import numpy as np
from vectorAndMatrixClasses import Vector, Matrix, linear_combination, myBeartype

Number = np.float32

def impl(u: "Vector", v: "Vector") -> Number:
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise ValueError("u and v must be vectors.")
    if u.size() != v.size():
        raise ValueError("u and v must have the same length.")

    scalar = np.float32(0.0)
    for x, y in zip(u.values, v.values):
        scalar = np.float32(scalar + np.float32(x) * np.float32(y))
    return scalar

def main():
    try:
        v1 = Vector([np.float32(-1), np.float32(6)])
        v2 = Vector([np.float32(3), np.float32(2)])
        print(impl(v1, v2))


    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
