
def bubbleSort(lista):
  tamanho = len(lista)

  for i in range(tamanho):
    for j in range(1, tamanho - i):
      if lista[j - 1] > lista[j]:
        lista[j - 1], lista[j] = lista[j], lista[j - 1]

  return lista
