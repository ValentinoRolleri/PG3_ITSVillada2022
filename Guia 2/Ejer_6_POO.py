class Familia:

    def __str__(self):

        self.madre = input("Nombre de la madre: ")
        self.padre = input("nNombre del padre: ")
        self.hijos = []
        self.hijos.append(input("Nombre del hijo: "))

        if (self.hijos == "0"):

            pass

    def mostrar(self):

        print("Madre: ", self.madre)
        print("Padre: ", self.padre)
        print("Hijos: ", self.hijos)

Familia1 = Familia()

Familia1.mostrar()