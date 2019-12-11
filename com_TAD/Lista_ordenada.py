
class Lista_ordenada:

  def __init__(self):
    self.lista = []


  def tamanho(self):
    return len(self.lista)


  def inserir(self, elemento):

    for i in range(self.tamanho()):
      if elemento < self.lista[i]:
        self.lista = self.lista[:i] + [ elemento ] + self.lista[i:]
        break
      if elemento == self.lista[i]: # não permite elementos repetidos
        break
    else:
      self.lista += [ elemento ]

  def busca(self, elemento):

    for elm in self.lista:
      if elemento == elm:
        return True
    
    return False

  def converter_para_string(self):
    return '  '.join(self.lista)
