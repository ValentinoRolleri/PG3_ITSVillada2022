class triangulo:

    def datos(self, lado1, lado2, lado3):

        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def mayor(self):

        lista = [self.lado1, self.lado2, self.lado3]
        lista.sort()
        print(lista[0])
    
    def equilatero(self):

        if self.lado1 == self.lado2 & self.lado1 == self.lado3:
            print("El triangulo es equilatero")

        else:
            print("El triangulo no es equilatero")

t1 = triangulo()

t1.datos(3,2,4)

t1.mayor()

t1.equilatero()