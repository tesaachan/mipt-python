from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, data):
        self.data = list()
        for i in data:
            self.data.append(list(i))

    def __str__(self):
        ans = ""
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                sign = '\t'
                if j == len(self.data[i]) - 1:
                    sign = '\n'
                    if i == len(self.data) - 1:
                        sign = ''
                ans += str(self.data[i][j]) + sign
        return ans
        # return '\n'.join(['\t'.join(map(str, list)) for list in self.data])

    def size(self):
        return (len(self.data), len(self.data[0]))

    def __add__(self, other):
        if len(self.data) != len(other.data) or not all(
            map(
                lambda n, m: len(n) == len(m),
                self.data, other.data
            )
        ):
            raise MatrixError(self, other)
        return Matrix(
            list(
                map(
                    lambda n, m: map(
                        lambda x, y: x + y,
                        n, m
                    ),
                    self.data, other.data
                )
            )
        )

    def __mul__(self, number):
        return Matrix(
            list(
                map(
                    lambda n: n * number,
                    line
                ) for line in self.data
            )
        )

    __rmul__ = __mul__

    def transpose(self):
        self.data = list(list(el) for el in zip(*self.data))
        return Matrix(self.data)

    @staticmethod
    def transposed(self):
        new_Matrix = Matrix(self.data)
        return Matrix(list(list(el) for el in zip(*new_Matrix.data)))

exec(stdin.read())
