from __future__ import annotations
from typing import TypeVar, Generic, List, Union
from dataclasses import dataclass
from typing import Tuple

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
                
    def __str__(self):
        lines = []
        for row in self.rows:
            formatted = [0.0 if my_abs(x) < 1e-10 else x for x in row]
            lines.append(str(formatted))
        return "\n".join(lines)

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
        rows = len(self.rows)
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

    def mul_vec(self, vec: "Vector")-> "Vector":
        if not isinstance(vec, Vector):
            raise ValueError("Argument must be a vector.")
        
        n_rows, n_columns = self.shape()
        if n_columns != vec.size():
            raise ValueError("Vector length must match the number of columns in the matrix.")

        newVector = []
        for row in self.rows:
            res = 0
            for coeff, val in zip(row, vec.values):
                res += coeff * val
            newVector.append(res)
        
        return(Vector(newVector))

    def transpose(self)-> "Matrix":
        transposed = [list(row) for row in zip(*self.rows)]
        return Matrix(transposed)

    def mul_mat(self, v: "Matrix") -> "Matrix":
        rows1, columns1 = self.shape()
        rows2, columns2 = v.shape()
        if not isinstance(v, Matrix):
            raise ValueError("Argument must be a Matrix.")
        if columns1 != rows2:
            raise ValueError("Number of columns of the first matrix must equal number of rows of the second matrix.")
        
        v_t = v.transpose(True)
        newMatrix = []
        for row1 in self.rows:
            newRow = []
            v_row1 = Vector(row1)
            for row2 in v_t.rows:
                newRow.append(v_row1.dot(Vector(row2)))
            newMatrix.append(newRow)
        
        return Matrix(newMatrix)
            
    def trace(self)-> Number:
        if not self.is_square():
            raise ValueError("The matrix must be a square.")
        
        rows , columns = self.shape()
        total = 0

        for i in range(columns):
            total += self.rows[i][i]

        return total
    
    def find_first_pivot(self)-> Tuple[int, int, bool]:
        transposed_matrix = self.transpose()
        pivot = -1
        position_row = -1
        position_column = -1
        for i, row in enumerate(transposed_matrix.rows):
            for j, column in enumerate(row):
                if my_abs(column) > 0:
                    pivot = my_abs(column)
                    position_column = i
                    position_row = j
                    break
            if pivot > 0:
                break
        
        one_or_not = True if self.rows[position_row][position_column] == 1 else False
        
        return position_row, position_column, one_or_not

    def turn_pivot_to_one(self, v: List, column : int)-> List:
        v_copy = Vector(v)
        mult = 1/v_copy.values[column]
        v_copy.scl(mult)
        return v_copy.values

    def under_pivot_to_zero(self, v: List, v_pivot: List, target_pos: int)-> List:
        v_vector = Vector(v)
        v_pivot_vector = Vector(v_pivot)
        target = v[target_pos]
        v_pivot_vector.scl(target)
        v_vector.sub(v_pivot_vector)

        return v_vector.values
    
    def line_is_full_of_zero(self, v: List)-> bool:
        return all(element == 0 for element in v)

    def find_pivot_position(self, v: List)-> int:
        i = 0

        for element in v:
            if element == 0:
                i += 1
            else:
                break
        
        return i
            
    def swap_all_line_with_zero_at_the_end(self, m: "Matrix")-> "Matrix":
        line_with_0 = 0
        newMatrix = []
        to_copy = []
        highest = -1

        for row_nb in range(len(m.rows)):
            if highest < self.find_pivot_position(m.rows[row_nb]):
                highest = self.find_pivot_position(m.rows[row_nb])
            if self.line_is_full_of_zero(m.rows[row_nb]):                    
                line_with_0 += 1
                if len(to_copy) == 0:
                    to_copy = m.rows[row_nb]
            else:
                newMatrix.append(m.rows[row_nb])


        newMatrixOrdered = []
        if highest > 0:
            for i in range(highest + 1):
                for row_nb in range(len(newMatrix)):
                    if i == self.find_pivot_position(newMatrix[row_nb]):
                        newMatrixOrdered.append(newMatrix[row_nb])
        else:
            newMatrixOrdered = newMatrix

        for i in range(line_with_0):
            newMatrixOrdered.append(to_copy)

        return Matrix(newMatrixOrdered)
        

    def reversed_row_echeleon_form(self, m: "Matrix")-> "Matrix":
        for i in range(len(m.rows)-1, -1, -1):
            pivot_pos = self.find_pivot_position(m.rows[i])
            if self.line_is_full_of_zero(m.rows[i]):
                continue            
            for previous_row in range(i - 1, -1, -1):
                m.rows[previous_row] = self.under_pivot_to_zero(m.rows[previous_row], m.rows[i], pivot_pos)

        return Matrix(m)

    def rank(self)-> "Matrix":
        position_row , position_column, one_or_not = self.find_first_pivot()

        if position_row == -1 and position_column == -1:
            print("The matrix is already an reversed row echelon form")
            return
        
        matrix_cpy = Matrix(self.rows)
        matrix_cpy = self.swap_all_line_with_zero_at_the_end(matrix_cpy)
        rows_nb, column_nb = matrix_cpy.shape()

        for row_nb in range(len(matrix_cpy.rows)):
            if self.line_is_full_of_zero(matrix_cpy.rows[row_nb]):
                continue
            pivot_pos = self.find_pivot_position(matrix_cpy.rows[row_nb])
            matrix_cpy.rows[row_nb] = self.turn_pivot_to_one(matrix_cpy.rows[row_nb], pivot_pos)
            for next_row_nb in range(row_nb + 1, len(matrix_cpy.rows)):
                if self.find_pivot_position(matrix_cpy.rows[next_row_nb]) != pivot_pos:
                        continue
                matrix_cpy.rows[next_row_nb] = self.under_pivot_to_zero(matrix_cpy.rows[next_row_nb] ,matrix_cpy.rows[row_nb], pivot_pos)            
            matrix_cpy = self.swap_all_line_with_zero_at_the_end(matrix_cpy)

        line_with_0 = 0
        for row_nb in range(len(matrix_cpy.rows)):
            if self.line_is_full_of_zero(matrix_cpy.rows[row_nb]):
                line_with_0 += 1 


        return rows_nb - line_with_0
        
            











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

    def norm_1(self) -> Number:
        """
        Formula: ||v||₁ = Σ |vᵢ|
        """
        sum = 0
        for x in self.values:
            if x < 0:
                x = -x
            sum += x
        
        return sum

    def norm(self) -> Number:
        """
        Formula: ||v||₂ = sqrt(Σ (vᵢ)²)
        """
        sum = 0
        for x in self.values:
            if x < 0:
                x = -x
            sum += pow(x, 2)
        return sum ** 0.5

    def norm_inf(self) -> Number:
        """
        Formula: ||v||∞ = max(|vᵢ|) 
        """
        max = 0
        for x in self.values:
            if x < 0:
                x = -x
            if x > max:
                max = x
        return max

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

    
def my_abs(n: Number)-> Number:
    if n >= 0:
        return n
    else :
        return -n