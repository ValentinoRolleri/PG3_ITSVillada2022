palabra = input("Ingrese una palabra: ")

def contar_vocales(palabra):
	contador = 0

	for letra in palabra:

		if letra.lower() in "a e i o u":
			contador += 1 

	return contador

cantidad = contar_vocales(palabra)

print(f"En {palabra} hay: {cantidad} vocales")