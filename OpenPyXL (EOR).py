from datetime import datetime
from math import log
from math import ceil
from openpyxl import Workbook
from openpyxl.styles import Font, Border, Side

book = Workbook()
sheet = book.active


variables = []
fa = []


def añadirfa(pos,realizar):
    if(realizar):
        fa.append(1)
    else:
        fa[pos] = fa[pos] + 1
        
        
def cuadro():
    tam = len(variables)
    print(tam)
    
    
    #Primer Escalon
    sheet[f"B{2}"] = "Variables"
    sheet[f"B{3+tam}"] = "Totales"
    for k in range(0,tam):
        sheet[f"B{3+k}"] = variables[k]

    #Segundo Escalon
    sheet[f"C{2}"] = "fa"
    sheet[f"C{3+tam}"] = sumar(fa)
    for k in range(0,tam):
        sheet[f"C{3+k}"] = fa[k]

    #Tercer Escalon
    sheet[f"D{2}"] = "fr"
    sheet[f"D{3+tam}"] = 1
    for k in range(0,tam):
        sheet[f"D{3+k}"] = f"{fa[k]}/{sumar(fa)} = {fa[k]/sumar(fa)}"

    #Cuarto Escalon
    sheet[f"E{2}"] = "fp"
    sheet[f"E{3+tam}"] = "100%"
    for k in range(0,tam):
        sheet[f"E{3+k}"] = f"{fa[k]/sumar(fa)*100}%"
        
    #Quinto Escalon
    valor = 0
    sheet[f"F{2}"] = "fr"
    for k in range(0,tam):
        valor = valor + fa[k]
        sheet[f"F{3+k}"] = valor


    #Titulo de pagina
    now = datetime.now()
    date_time = now.strftime("%d.%m.%Y")
    sheet.title = date_time

    
    
    
    book.save("estadistica.xlsx")

def sumar(lista):
    suma = 0
    for l in lista:
        suma = suma + l
    return suma

def numMayor(lista):
    mayor = lista[0]
    for i in lista:
        if(i>mayor):
            mayor = i
    return mayor

def numMenor(lista):
    menor = lista[0]
    for i in lista:
        if(i<menor):
            menor = i
    return menor

def cantIntervalos(lista):
    return ceil(1+(log(len(lista),10)*3.322))

def valorAmplitud(lista,k):
    mayor = numMayor(lista)
    menor = numMenor(lista)
    return ceil((mayor-menor)/k)


def pasarGrafica(lista,k,a):
    while True:
        minimo = numMenor(lista)
        maximo = numMayor(lista)
        valor = ""
        for i in range(0,k):
            valor = f"[{minimo + a*i} , {minimo + a*i + a})"
            fa.append(0)
            for j in lista:
                if(j>=minimo + a*i and j<minimo + a*i + a):
                    fa[i] = fa[i] + 1
            variables.append(valor)
        print(variables)
        print(fa)
        break
    cuadro()



def graficaNormal():
    print("Ingrese una lista de números:")
    list = input(">> ")

    cont = 0
    for i in list:
        if(cont==0):
            variables.append(i)

            añadirfa(cont,True)
            

        else:
            cont2=0
            for j in variables:
                if(j==i):
                    posicion = variables.index(i)
                    añadirfa(posicion,False)
                    break
                else:
                    cont2+=1
                    if(cont2==len(variables)):
                        variables.append(i)
                        añadirfa(len(variables),True)
                        break
        cont+=1
    cuadro()

def graficaIntervalos():
    cont = 0
    lista = []
    while True:
        print(f"Ingrese el {cont+1}° numero: (pulsa enter para terminar)")
        
        num = input(">> ")
        if(num==""):
            break
        else:
            lista.append(int(num))
        cont+=1

    k = cantIntervalos(lista)
    while True:
        print(f"Elija la CANTIDAD DE INTERVALOS:")
        print(f"1) Automatico ({k})")
        print(f"2) Manual")
        num = input(">> ")
        if(num == 2):
            print(f"Ingrese el numero de intervalos:")
            k = int(input(">> "))
        break
        


    a = valorAmplitud(lista,k)
    while True:
        print(f"Elija la AMPLITUD:")
        print(f"1) Automatico ({a})")
        print(f"2) Manual")
        num = input(">> ")
        if(num == 2):
            print(f"Ingrese el numero de intervalos:")
            a = int(input(">> "))
        break
    pasarGrafica(lista,k,a)
    


    
graficaIntervalos()