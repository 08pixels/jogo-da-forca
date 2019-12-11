
class Lista:

  # def __init__(self):
  #   self.inicio = 0
  #   self.fim = 0
  #   self.lista = []

  def __init__(self, lista):
    self.inicio = 0
    self.fim = len(lista)
    self.lista = lista

  # def tamanho(self):
  #   return self.fim


  def esta_vazia(self):
    return self.inicio == self.fim


  # def inserir(self, elemento):
  #   self.lista += [ elemento ]
  #   self.fim += 1


  def remover(self):
    if not self.esta_vazia():
      self.inicio += 1
    else:
      return -1


  def get_elemento(self):

    if not self.esta_vazia():
      valor = self.lista[self.inicio]
      return valor
    else:
      return 'a lista está vazia'


