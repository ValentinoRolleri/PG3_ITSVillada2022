lista = [0, 2, 18, 24, 33, 42, 100]

print (lista)

buscar = int(input("Que numero quiere buscar en la lista: "))

def funcion(lista, buscar):

    if buscar in lista:
        print(lista.index(buscar))

    else:
        print ("El numero ingresado no esta en la lista: ")

funcion(lista, buscar)









