class Numeros:
    def __init__(self, numeros):
        self.numeros = numeros

    def imprimir(self):
        for numero in self.numeros:
            if numero % 2 != 0 and numero > 3:
                print(numero, end=' ')
        print()

numeros = [1, 5, 8, 3, 30, 9, 13]

num = Numeros(numeros)
num.imprimir()


