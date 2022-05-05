igual = 0

indice = 0

texto = input("Palabra a evaluar: ")

def funcion(igual, indice):

    for ind in reversed(range(0, len(texto))):

        if texto[ind].lower() == texto[indice].lower():
            igual += 1

        indice += 1

    if len(texto) == igual:
        print("Si es capicua")

    else:
        print("No es capicua")

funcion(igual, indice)