from jogo import forca

jogo_da_forca = forca()

while True:
  jogo_da_forca.limpar_tela()
  jogo_da_forca.mostrar_tela_inicial()
  opcao = input()

  if opcao == '1':
    jogo_da_forca.limpar_tela()
    jogo_da_forca.iniciar()
    jogo_da_forca.mostrar_estado()
    
    while True:
      tentativa = input('%20s : ' %('SUA JOGADA'))

      jogo_da_forca.jogar(tentativa)
      jogo_da_forca.limpar_tela()
      estado = jogo_da_forca.mostrar_estado()

      if(estado == forca.FIM_DE_JOGO):
        break

  elif opcao == '2':
    jogo_da_forca.limpar_tela()
    break
