from typing import Union
from vectorAndMatrixClasses import Vector, Matrix, linear_combination, myBeartype

Number = Union[int, float]

def norm_1(v: "Vector") -> Number:
    """
    Formula: ||v||₁ = Σ |vᵢ|
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
    Formula: ||v||₂ = sqrt(Σ (vᵢ)²)
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
    Formula: ||v||∞ = max(|vᵢ|) 
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

def main():
    try:
        v1 = Vector([0., 0., 0.])
        print(f"{norm_1(v1)}, {norm(v1)}, {norm_inf(v1)}")
        v1 = Vector([1., 2., 3.])
        print(f"{norm_1(v1)}, {norm(v1)}, {norm_inf(v1)}")
        v1 = Vector([-1., -2.])
        print(f"{norm_1(v1)}, {norm(v1)}, {norm_inf(v1)}")


    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
