class Buscador:
    def __init__(self, lista):
        self.lista = lista

    def buscar_numero(self, numero):
        if numero in self.lista:
            posicion = self.lista.index(numero)
            return f"El número {numero} se encuentra en la posición {posicion}."
        else:
            return f"El número {numero} no existe en la lista."


num = [20, 15, 12, 11, 8, 4, 1]
buscar = int(input("Ingresa el número: "))
buscador = Buscador(num)
resultado = buscador.buscar_numero(buscar)
print(resultado)


