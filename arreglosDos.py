class Nombres:
    def __init__(self, tamano):
        self.tamano = tamano
        self.nombres = []
        self.longitudes = []
        self.rellenar()

    def rellenar(self):
        for i in range(self.tamano):
            nombre = input(f"\nIngresa el nombre {i + 1}: ")
            self.nombres.append(nombre)
            self.longitudes.append(len(nombre))

    def mostrar(self):
        print("\nNombres:", self.nombres)
        print("\nLongitudes:", self.longitudes)

tamano = int(input("\nIndica número de nombres: "))

nombres = Nombres(tamano)
nombres.mostrar()


