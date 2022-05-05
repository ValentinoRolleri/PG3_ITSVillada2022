año = int(input("Escriba un año: "))

def bisiesto(num):

    if not año % 4 and (año % 100 or not año % 400):
        print("Ese año si es bisiesto")

    else:
        print("Ese año no es bisiesto")

bisiesto(año)