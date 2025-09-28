from __future__ import annotations
from typing import TypeVar, Generic, List, Union
from dataclasses import dataclass

K = TypeVar("K")
Number = Union[int, float]

def myBeartype(arg: object, expected_type: type, element_type: type = None) -> None:
    if not isinstance(arg, expected_type):
        raise TypeError(f"The argument must be of type {expected_type.__name__}")
    if element_type is not None:
        if not all(isinstance(x, element_type) for x in arg):
            raise TypeError(f"All elements must be of type {element_type.__name__}")
        
# --------------------------- MATRIX CLASS ---------------------------

@dataclass
class Matrix(Generic[K]):
    rows: List[List[Number]]

    def __post_init__(self):
        if not self.rows:
            raise ValueError("Matrix cannot be empty")

        if not all(isinstance(r, list) for r in self.rows):
            raise TypeError("Matrix must be initialized with a list of lists")

        row_length = len(self.rows[0])
        if any(len(r) != row_length for r in self.rows):
            raise ValueError("All rows must have the same length")

        for r in self.rows:
            if not all(isinstance(x, (int, float)) for x in r):
                raise TypeError("Matrix elements must be int or float")
                
        
    def shape(self) -> tuple[int, int]:
        rows = len(self.rows)
        columns = len(self.rows[0])
        return rows, columns

    def print_shape(self) -> None:
        if self.rows:
            print( f"({len(self.rows)}, {len(self.rows[0])})")
        else:
            print("Empty Matrix")

    def is_square(self) -> bool:
        rows = self.rows
        columns = len(self.rows[0])
        return rows == columns
    
    def print_is_square(self) -> None:
        rows = len(self.rows)
        columns = len(self.rows[0])
        print(rows == columns)
    
    def print_matrix(self) -> None:
        self.print_shape()
        for rows in self.rows:
            print(rows)
    
    def reshape(self) -> Vector[K]:
        newList = []
        rowsLen = len(self.rows)
        columnsLen = len(self.rows[0])
        for j in range(columnsLen):
            for i in range(rowsLen):
                newList.append(self.rows[i][j])
                
        return Vector(newList)

    def add(self, other: "Matrix[K]") -> None:
        myBeartype(other, type(self))
        if other.shape() != self.shape():
            raise ValueError("Matrixes must have the same size.")
    
        self.rows = [
                [x + y  for x, y in zip(xrows, yrows)]
                for xrows, yrows in zip(self.rows, other.rows)]
        
        

    def sub(self, other: "Matrix[K]") -> None:
        myBeartype(other, type(self))

        if other.shape() != self.shape():
            raise ValueError("Matrixes must have the same size.")
    
        self.rows = [
                [x - y  for x, y in zip(xrows, yrows)]
                for xrows, yrows in zip(self.rows, other.rows)]
        
    
    def scl(self, scalar: Number) -> None:
        myBeartype(scalar, Number)

        self.rows = [
            [x * scalar for x in rows] 
            for rows in self.rows
            ]

# --------------------------- VECTOR CLASS ---------------------------

@dataclass
class Vector(Generic[K]):
    values: List[Number]

    def __post_init__(self):
        if not self.values:
            raise ValueError("Vector cannot be empty")
        if not all(isinstance(x, Number) for x in self.values):
            raise TypeError("All elements of Vector must be numbers")
        
    def size(self) -> int:
        return len(self.values)

    def print_size(self) -> int:
        print("The size of the vector is :",len(self.values))

    def print_vector(self):
        self.print_size()
        print(self.values)

    def reshape(self, rows: int, columns: int, order="col") -> "Matrix[K]":
        if columns <= 0:
            raise ValueError("columns must be > 0")
        if rows * columns != self.size():
            raise ValueError("Invalid reshape: incompatible dimensions.")
        
        if order == "col":
            newMatrix = []
            for i in range(0, rows):
                newRows = []
                for j in range(0, self.size(), rows):
                    newRows.append(self.values[i+j])
                newMatrix.append(newRows)
        elif order == "row":
            newMatrix = [
                self.values[i: i+columns]
                for i in range(0, len(self.values), columns)
            ]
        else:
            raise ValueError("order must be 'row' or 'col'")            
            
        return Matrix(newMatrix)

    def add(self, other: "Vector[K]") -> None:
        myBeartype(other, type(self))
        if other.size() != self.size():
            raise ValueError("Vectors must have the same length.")
        
        self.values = [x + y for x,y in zip(self.values, other.values)]


    def sub(self, other: "Vector[K]") -> None:
        myBeartype(other, type(self))
        if other.size() != self.size():
            raise ValueError("Vectors must have the same length.")
        
        self.values = [x - y for x,y in zip(self.values, other.values)]


    def scl(self, scalar: Number) -> None:
        myBeartype(scalar, Number)
        self.values = [x * scalar for x in self.values]

    def dot(self, v: "Vector") -> Number:
        if not isinstance(v, Vector):
            raise ValueError("v must be vectors.")
        if self.size() != v.size():
            raise ValueError("Both vectors must have the same length.")

        scalar = 0
        for x, y in zip(self.values, v.values):
            scalar = (scalar + x * y)
        return scalar


# --------------------------- Function ---------------------------

def linear_combination(vectors: List["Vector[K]"], scalars: List[Number]) -> "Vector[K]":
    myBeartype(vectors, list, Vector)
    myBeartype(scalars, list, Number)

    if len(vectors) != len(scalars):
        raise ValueError("Vectors and scalars must have the same length.")
    
    row_length = vectors[0].size()
    if any(r.size() != row_length for r in vectors):
        raise ValueError("All Vectors must have the same length.")
    
    newVector = []
    for i in range(vectors[0].size()):
        result = 0
        for v, s in zip(vectors, scalars):
            result += v.values[i] * s
        newVector.append(result)

    print(newVector)

    
