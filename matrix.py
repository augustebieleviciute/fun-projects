import numpy as np

A = np.array([[1,7,3],[7,4,-5],[3,-5,6]])
B = np.array([[2,0,0],[0,1,0],[0,0,1]])
C = np.array([[5,0,0],[0,0,0],[0,0,0]])
D = np.array([1, 2, 2])
print(A)
print(B)

class Matrix:
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.sum = np.add(self.matrix1,self.matrix2)
        self.det = np.linalg.det(self.matrix1)
        self.transpose = np.transpose(self.matrix1)
        self.inverse = np.linalg.inv(self.matrix1)
        self.hermconj = np.conj(np.transpose(self.matrix1))
        self.trace = np.trace(self.matrix1)


        self.product = None
        self.type = ""
        self.eigen = None

    def product(self):
        compare = np.delete(self.matrix1, 0) == np.zeros_like(np.delete(self.matrix2, 0))
        if compare.all():
            self.product = self.matrix1[0][0] * self.matrix2
        else:
            self.product = self.matrix1@self.matrix2

    def type(self):
        if self.det == 0:
            self.type = self.type + " singular"
        compare = self.transpose == self.inverse
        if compare.all():
            self.type = self.type + " orthagonal"

        compare = self.hermconj @ self.matrix1 == np.identity(self.matrix1.shape[0])
        if compare.all():
            self.type = self.type + " unitary"

        compare = self.hermconj == self.matrix1
        if compare.all():
            self.type = self.type + " hermitian"

        compare = self.transpose == self.matrix1
        if compare.all():
            self.type = self.type + " symmetric"

        print(type)


    def eigen(self):
        self.eigen = np.linalg.eig(A)

abmatrix = Matrix(A, B)
print(abmatrix.sum())