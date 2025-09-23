from typing import Union
from vectorAndMatrixClasses import Vector, Matrix, linear_combination, myBeartype

Number = Union[int, float]

def norm_1(v: "Vector") -> Number:
    """
    Formula: ∥v∥₁ = Σ |vᵢ|
    """
    if not isinstance(v, Vector):
        raise ValueError("v must be a vector.")
    
    sum = 0
    for x in v.values:
        if x < 0:
            x = -x
        sum += x
    
    return sum


def norm(v: "Vector") -> Number:
    """
    Formula: ∥v∥₂ = sqrt(Σ (vᵢ)²)
    """
    if not isinstance(v, Vector):
        raise ValueError("v must be a vector.")
    
    sum = 0
    for x in v.values:
        if x < 0:
            x = -x
        sum += pow(x, 2)
    return sum ** 0.5

def norm_inf(v: "Vector") -> Number:
    """
    Formula: ∥v∥∞ = max(|vᵢ|) 
    """
    if not isinstance(v, Vector):
        raise ValueError("v must be a vector.")
    
    max = 0
    for x in v.values:
        if x < 0:
            x = -x
        if x > max:
            max = x
    return max

def impl(u: "Vector", v: "Vector") -> Number:
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise ValueError("u and v must be vectors.")
    if u.size() != v.size():
        raise ValueError("u and v must have the same length.")

    scalar = 0
    for x, y in zip(u.values, v.values):
        scalar = (scalar + x * y)
    return scalar

def angle_cos(u: "Vector", v: "Vector") -> Number:
    """
    cos(θ) = (u * v)/(∥u∥ * ∥v∥)
    """
    if not isinstance(u, Vector) or not isinstance(v, Vector):
        raise ValueError("u and v must be vectors.")
    if u.size() != v.size():
        raise ValueError("u and v must have the same length.")
    
    angle = 0

    top_side = impl(u, v)
    bottom_side = norm(u) * norm(v)
    angle = top_side/bottom_side

    return angle
    





def main():
    try:
        v1 = Vector([1., 0.])
        v2 = Vector([1, 0])
        print(angle_cos(v1, v2))

        v1 = Vector([1., 0.])
        v2 = Vector([0, 1])
        print(angle_cos(v1, v2))

        v1 = Vector([-1., 1.])
        v2 = Vector([ 1., -1.])
        print(angle_cos(v1, v2))

        v1 = Vector([2., 1.])
        v2 = Vector([4., 2.])
        print(angle_cos(v1, v2))
        
        v1 = Vector([1., 2., 3.])
        v2 = Vector([4., 5., 6.])
        print(angle_cos(v1, v2))

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
