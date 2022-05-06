class persona:

    def __init__(self):

        self.nombre = input("ingrese un nombre: ")
        self.edad = int(input("ingrese una edad: "))

    def prints(self):

        print("nombre: ",self.nombre," edad: ",self.edad)


class empleado(persona):

    def __init__(self):

        super().__init__()
        self.salario = int(input("introduzca el salario mensual: "))
        self.impuestos()

    def impuestos(self):

        if self.salario >= 3000:
            print("vas a tener que pagar un 10% por impuestos")

        else:
            print("no tenes que pagar nada en impuestos")

p1 = persona()

p1.prints()

e1 = empleado()