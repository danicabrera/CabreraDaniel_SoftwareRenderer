class Matriz():
    fila1 = [0, 0, 0, 0]
    fila2 = [0, 0, 0, 0]
    fila3 = [0, 0, 0, 0]
    fila4 = [0, 0, 0, 0]

    def __init__(self):


        matriz = [fila1, fila2, fila3, fila4]

    def crear(self, fila1 = [0,0,0,0], fila2 = [0,0,0,0], fila3 = [0,0,0,0], fila4 = [0,0,0,0]):
        self.matriz = [fila1, fila2, fila3, fila4]
        return self.matriz

    """def multValor(self, valor):

        for i in self.fila1:
            self.fila1[i] = self.fila1[i] * valor

        for i in self.fila2:
            self.fila2[i] = self.fila2[i] * valor

        for i in self.fila3:
            self.fila3[i] = self.fila3[i] * valor

        for i in self.fila4:
            self.fila4[i] = self.fila4[i] * valor

        return self"""

    def identidad(self):
        self.matriz = Matriz.crear(self, fila1 = [1,0,0,0], fila2 = [0,1,0,0], fila3 = [0,0,1,0], fila4 = [0,0,0,1])
        return self.matriz

    def multMatrices(self, matr1, matr2):
        matrizResultado = Matriz()

        matrizResultado.crear(self, fila1=[0,0,0,0], fila2= [0,0,0,0], fila3= [0,0,0,0], fila4=[0,0,0,0])

        for i in range(4):
            for j in range(4):
                for k in range(4):

                    matrizResultado[i][j] += matr1[i][k] * matr2[k][j]

        """for i in range(4):
            matrizResultado.fila1 = [(matr1.fila1[0] * matr2.fila1[0] + matr1.fila1[1] * matr2.fila2[0] + matr1.fila1[2] * matr2.fila3[0]), (), (), ()]
            matrizResultado.fila2 = []
            matrizResultado.fila3 = []
            matrizResultado.fila4 = []
            return matrizResultado """