ancho = int(input("Escriba el ancho del rectangulo: "))

alto = int(input("Escriba el alto del rectangulo: "))

caracter = input("Que caracter va a usar? : ")

def tabla():

    for i in range(alto):

        for j in range(ancho):
            print(caracter, end="")

        print()

tabla()