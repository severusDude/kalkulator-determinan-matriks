import string
import numpy as np
import scipy
from fractions import Fraction


def find_determinant(matrix: list) -> int:
    result = 0

    matrix_size = len(matrix)

    match matrix_size:
        case 2:
            a1 = matrix[0][0]
            a2 = matrix[0][1]
            b1 = matrix[1][0]
            b2 = matrix[1][1]

            # step 1, multiply operation inside parenthesses
            step1 = {
                "ad": a1*b2,
                "bc": a2*b1
            }

            # step 2, calculate result
            step2 = step1["ad"]-step1["bc"]

            result = round(step2, 2)

        case 3:
            a1 = matrix[0][0]
            a2 = matrix[0][1]
            a3 = matrix[0][2]
            b1 = matrix[1][0]
            b2 = matrix[1][1]
            b3 = matrix[1][2]
            c1 = matrix[2][0]
            c2 = matrix[2][1]
            c3 = matrix[2][2]

            # step 1, multiply operation inside parenthesses
            step1 = {
                "aei": a1*b2*c3,
                "bfg": a2*b3*c1,
                "cdh": a3*b1*c2,
                "ceg": a3*b2*c1,
                "bdi": a2*b1*c3,
                "afh": a1*b3*c2
            }

            # step 2, calculate result
            step2 = step1["aei"]+step1["bfg"]+step1["cdh"] - \
                step1["ceg"]-step1["bdi"]-step1["afh"]

            result = round(step2, 2)

        case _:
            pass

    return result


def determinant(matrix: list) -> int:
    """Calculate the matrix determinant of order of n using LU decomposition method"""
    lu, piv = scipy.linalg.lu_factor(matrix)

    return round(np.prod(np.diag(lu)), 2)


