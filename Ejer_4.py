def bubblesort(elements):

  for n in range(len(elements)-1, 0, -1):

    for i in range(n):

      if elements[i] < elements[i + 1]:
        elements[i], elements[i + 1] = elements[i + 1], elements[i]

elements = [88, 4, 55, 673, 9, 45, 0, 12]
  
print("Desordenada: ") 

print(elements)

bubblesort(elements)

print("Ordenada: ")

print(elements)