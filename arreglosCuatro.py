class Notas:
    def __init__(self, notas):
        self.notas = notas

    def eliminar(self):
        menor = self.notas[0]
        for nota in self.notas:
            if nota < menor:
                menor = nota
        self.notas.remove(menor)
        return menor

    def calcular(self):
        suma = sum(self.notas)
        promedio = suma / len(self.notas)
        return promedio

    def mostrar(self):
        menor = self.eliminar()
        print(f"\nNota más baja: {menor}")
        promedio = self.calcular()
        print(f"\nPromedio de las notas: {promedio:.2f}")

num = [20, 15, 12, 11, 8, 4, 1]

notas = Notas(num)
notas.mostrar()


