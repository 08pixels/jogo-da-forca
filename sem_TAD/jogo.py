import random
import os
import text
import ordenacao

class forca:
  TENTATIVA_MAXIMA = 6 # quantidade de 'frames' do 'sprite sheet' do personagem
  VAZIO = '___'
  FIM_DE_JOGO = 0
  CONTINUA_JOGO = 1

  def __init__(self):
    self.palavras = text.palavras_secretas
    self.personagem = text.ascii_personagem
    self.iniciar()

  def status_do_jogo(self):

    # verifica gameover
    if not self.chance:
      print('\n\nA FRUTA ERA: %s' %(self.palavra))
      self.mostrar_fim_jogo(text.voce_perdeu)
      return forca.FIM_DE_JOGO
    
    # verifica campeao
    if not self.descobertas.count(False):
      self.mostrar_fim_jogo(text.voce_venceu)
      return forca.FIM_DE_JOGO

    # status continua o mesmo
    return forca.CONTINUA_JOGO


  def mostrar_tela_inicial(self):
    print(text.jogo_da_forca)
    print(text.opcoes)


  def mostrar_estado(self):
    # cálculo do 'spread sheet' do personagem
    chance = forca.TENTATIVA_MAXIMA - self.chance
    personagem = self.personagem[chance]
    
    # a visão do jogador em relação as letras descobertas
    descobertas = [self.palavra[posicao].upper() if valor else forca.VAZIO
                  for posicao, valor in enumerate(self.descobertas)]
    descobertas = '  '.join(descobertas)

    tentadas = ordenacao.bubbleSort(self.tentadas)
    tentadas = '  '.join(tentadas)

    print(personagem)
    print('%20s : %s' %('TENTATADAS %d/%d' %(chance, forca.TENTATIVA_MAXIMA), tentadas))
    print('%20s : %3s' %('É UMA FRUTA', descobertas) )

    return self.status_do_jogo()


  def iniciar(self):
    self.chance = 6
    self.tentadas = []
    self.palavra = self.escolher_proxima_palavra()
    self.descobertas = [False] * len(self.palavra)


  def jogar(self, letra): 
    if letra == '':
      return

    # se o usuário passar uma sequência de letras
    # é considerada somente a primeira
    letra = letra[0].lower()

    # verifica se realmente é uma letra
    if letra >= 'a' and letra <= 'z':

      if letra in self.palavra:
        # atualização das letras descobertas
        for posicao in range(len(self.palavra)):
          if letra == self.palavra[posicao]:
            self.descobertas[posicao] = letra.upper()
      
      # atualização das letras erradas
      elif letra not in self.tentadas:
        self.tentadas.append(letra)
        self.chance -= 1


  def escolher_proxima_palavra(self):
    posicao = random.randint(0, len(self.palavras) - 1)
    return self.palavras[posicao]


  def mostrar_fim_jogo(self, mensagem):
    print(mensagem)
    input('pressione qualquer tecla para continuar...')


  def limpar_tela(self):
    # comando windows e linux
    os.system('cls' if os.name == 'nt' else 'clear')
