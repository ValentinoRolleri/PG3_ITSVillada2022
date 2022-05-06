class Operaciones:

    def __init__(self):

        self.num1 = int(input("Ingrese un numero: "))
        self.num2 = int(input("Ingrese otro numero: "))
        self.suma = self.num1 + self.num2
        self.resta = self.num1 - self.num2
        self.multiplicacion = self.num1 * self.num2
        self.division = self.num1 / self.num2

    def mostrar(self):

        print("La suma es: ", self.suma)
        print("La resta es: ", self.resta)
        print("La multiplicacion es: ", self.multiplicacion)
        print("La division es: ", self.division)

Operaciones = Operaciones()

Operaciones.mostrar()