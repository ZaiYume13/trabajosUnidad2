class Multiplo:
    def __init__(self, tamano, multiplo):
        self.tamano = tamano
        self.multiplo = multiplo
        self.arreglo = self.crear()

    def crear(self):
        arreglo = []
        for i in range(1, self.tamano + 1):
            arreglo.append(i * self.multiplo)
        return arreglo

    def mostrar(self):
        for elemento in self.arreglo:
            print(elemento, end=' ')
        print()

tamano = int(input("\nIndica el tamaño: "))
multiplo = int(input("\nIndica el número para los múltiplos: "))

multiplo = Multiplo(tamano, multiplo)
multiplo.mostrar()

