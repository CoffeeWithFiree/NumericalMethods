import numpy as np


class NumericalMethodsSystemEquations:
    #Example matrix: np.array([1, 1, 1, 6],
#                       [1, -1, 2, 5],
#                       [2, -1, -1, -3])
    @staticmethod
    def GaussMethod(matrix):
        matrix = matrix.astype(float)
        n = matrix.shape[0]
        #straight
        for i in range(n - 1):
            if matrix[i][i] == 0:
                raise ZeroDivisionError("Zero leading element — you need to rearrange the rows.")
            for j in range(i + 1, n):
                multipl_num = matrix[j][i] / matrix[i][i]
                matrix[j, i:] -= multipl_num * matrix[i, i:]
        print(matrix)
        #Reverse
        answers = [0] * n

        for i in range(n - 1, -1, -1):
            answers[i] = matrix[i][-1]
            for j in range(i + 1, n):
                answers[i] -= matrix[i][j] * answers[j]
            answers[i] /= matrix[i][i]

        return answers
