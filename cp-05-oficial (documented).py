# Challenge

def inicializarTabuleiro():
    '''
    Função que cria o tabuleiro
    -------------------------------------------------------
    Parâmetros:
    - Não possui parâmetros
    -------------------------------------------------------
    Retornos:
    - Retorna a matriz "matriz"
    '''
    matriz = []
    for i in range(3):
        line = []
        for j in range(3):
            line.append("")
        matriz.append(line)
    return matriz



def imprimirTabuleiro(matriz):
    '''
    Função que Imprime o tabuleiro
    -------------------------------------------------------
    Parâmetros:
    - Utiliza a matriz "matriz" para imprimi-la
    -------------------------------------------------------
    Retornos:
    - Não retorna valores
    '''
    print("\n")
    for i in range(len((matriz))):
        print(f"{matriz[i]}")
    print("\n")




def imprimeMenuPrincipal():
    '''
    Função que imprime o Menu ao usuário
    -------------------------------------------------------
    Parâmetros:
    - Não tem parâmetro
    -------------------------------------------------------
    Retornos:
    - Retorna "r" como a resposta para o menu
    '''
    r = int(input("MENU\nSelecione um modo:\n (1)JxJ\n (2)JxMáquina (fácil) (Indisponível)\n (3)Fechar\n"))
    return r


def imprimePontuacao(p1, p2):
    '''
    Função que imprime a pontuação ao usuário
    -------------------------------------------------------
    Parâmetros:
    - Utiliza a variável "p1" (jogador 1) para mostrar a pontuação do jogador
    - Utiliza a variável "p2" (jogador 2) para mostrar a pontuação do jogador
    -------------------------------------------------------
    Retornos:
    - Não retorna valores
    '''
    print(f"\nPlacar\nJogador 1: {p1}\nJogador 2: {p2}\n")





def out(matriz, x, y):
    '''
     Função que trata o erro de OutOfRange
    -------------------------------------------------------
    Parâmetros:
    - Utiliza a variável "x" para identificar o eixo x
    - Utiliza a variável "y" para identificar o eixo y
    - Utiliza a variável "matriz" para passa-la como parâmetro
    -------------------------------------------------------
    Retornos:
    - Retorna um novo valor para "x"
    - Retorna um novo valor para "y"
    '''
    while x > 3 or x < 1 or y > 3 or y < 1:
        print("\nValor(es) inválido(s)\n")
        imprimirTabuleiro(matriz)
        x, y = coordenadas()
    return x, y
    


def posicaoValida(matriz, x, y):
    '''
    Função que trata o erro de posição ocupada
    -------------------------------------------------------
    Parâmetros:
    - Utiliza a variável "x" para identificar o eixo x
    - Utiliza a variável "y" para identificar o eixo y
    - Utiliza a variável "matriz" para avaliar o tabuleiro
    -------------------------------------------------------
    Retornos:
    - Retorna um novo valor para "x"
    - Retorna um novo valor para "y"
     '''
    while matriz[x - 1][y - 1] != "":
        print("\nPosição inválida\n")
        imprimirTabuleiro(matriz)
        x, y = coordenadas()
    return x, y




def valida(matriz, x, y):
    '''
    Função que identifica se há erro de OutOfRange ou de posição ocupada
    -------------------------------------------------------
    Parâmetros:
    - Utiliza a variável "x" para identificar o eixo x
    - Utiliza a variável "y" para identificar o eixo y
    - Utiliza a variável "matriz" para avaliar o tabuleiro
    -------------------------------------------------------
    Retornos:
    - Caso identifique 1 ou mais erros, retorna novos valores para "x"
    - Caso identifique 1 ou mais erros, retorna novos valores para "y"
    '''
    if x > 3 or x < 1 or y > 3 or y < 1:
        x, y = out(matriz, x, y)
    if matriz[x - 1][y - 1] != "":
        x, y = posicaoValida(matriz, x, y)
    return x, y




def leiaCoordenadaLinha():
    '''
    Função que inputa a coordenada "x" (linha)
    -------------------------------------------------------
    Parâmetros:
    - Não há parâmetro
    -------------------------------------------------------
    Retornos:
    - Retorna o valor de "x"
    '''
    x = int(input("Informe a linha em que deseja marcar: "))
    return x




def leiaCoordenadaColuna():
    '''
    Função que inputa a coordenada "y" (coluna)
    -------------------------------------------------------
    Parâmetros:
    - Não há parâmetro
    -------------------------------------------------------
    Retornos:
    - Retorna o valor de "y"
    '''
    y = int(input("Informe a coluna em que deseja marcar: "))
    return y



def coordenadas():
    '''
    Função que chama as funções para definir as coordenadas
    -----------------------------------------------------
    Parâmetros:
    - Não há parâmetro
    -------------------------------------------------------
    Retornos:
    - Retorna o valor de "x"
    - Retorna o valor de "y"
    '''
    x = leiaCoordenadaLinha()
    y = leiaCoordenadaColuna()
    return x, y




def jogar(rodada, matriz, x, y):
    '''
    Função que valida as posições e chama a função 'jogar'
    -------------------------------------------------------
    Parâmetros:
    - Utiliza a matriz "matriz" para posicionar a jogada
    - Utiliza a variável "rodada" para identificar o jogador
    - Utiliza a variável "x" para identificar o eixo x
    - Utiliza a variável "y" para identificar o eixo y
    -------------------------------------------------------
    Retornos:
    - Não retorna valores
    '''
    if rodada % 2 == 0:
        matriz[x - 1][y - 1] = "X"
    else:
        matriz[x - 1][y - 1] = "O"
    imprimirTabuleiro(matriz)



def jogadaUsuario(rodada, matriz, x, y):
    '''
    Função efetua a validação da jogada e joga no tabuleiro
    -------------------------------------------------------
    Parâmetros:
    - Utiliza a matriz "matriz"  para posicionar a jogada
    - Utiliza a variável "rodada" para identificar o jogador
    - Utiliza a variável "x" para identificar o eixo x
    - Utiliza a variável "y" para identificar o eixo y
    -------------------------------------------------------
    Retornos:
    - Não retorna valores
    '''
    x, y = valida(matriz, x, y)
    jogar(rodada, matriz, x, y)




def verificaVencedor(matriz):

    '''
    Função que verifica o vencedor do jogo
    -------------------------------------------------------
    Parâmetros:
    - Utiliza a matriz "matriz" para identificar as casas
    -------------------------------------------------------
    Retornos:
    - Retorna "end" em caso positivo
    '''

    for indice,linha in enumerate(matriz):
        for indice2,coluna in enumerate(linha):

            if matriz[indice][0] == matriz[indice][1] == matriz[indice][2] != "":
                return "end"

            elif matriz[0][indice2] == matriz[1][indice2] == matriz[2][indice2] != "":
                return "end"

            elif matriz[0][0] == matriz[1][1] == matriz[2][2] != "" or matriz[0][2] == matriz[1][1] == matriz[2][0] != "":
                return "end"




def mostraVencedor(rodada, p1, p2):
    '''
    Função que mostra o vencedor do jogo e pontua
    -------------------------------------------------------
    Parâmetros:
    - Utiliza a variável "rodada" para identificar o vencedor
    - Utiliza a variável "p1" (jogador 1) para pontuar
    - Utiliza a variável "p2" (jogador 2) para pontuar
    -------------------------------------------------------
    Retornos:
    - Retorna o novo valor de "p1" (jogador 1)
    - Retorna o novo valor de "p2" (jogador 2)
    '''
    if rodada % 2 == 0:
        j=1
        p1 += 1
    else:
        j=2
        p2 += 1
    print(f"\nJogador {j} venceu\n")
    return p1,p2



def verificaVelha(matriz):
    '''
    Função que verifica se o jogo se encerrou por velha
    -------------------------------------------------------
    Parâmetros:
    - Utiliza a matriz "matriz" para percorre-la
    -------------------------------------------------------
    Retornos:
    - Retorna "end" em caso positivo
    '''
    casas = 0
    for indice,linha in enumerate(matriz):
        for indice2,coluna in enumerate(linha):
            if matriz[indice][indice2] != "":
                casas += 1
    if casas == len(matriz)**2:
        print("\nDeu velha\n")
        return "end"


def reset(matriz,rodada,p1,p2,ver2):
    '''
    Função que reseta o jogo
    -------------------------------------------------------
    Parâmetros:
    - Utiliza a matriz "matriz" para criar uma nova matriz
    - Utiliza a variável "rodada" para decidir qual jogador começará
    - Utiliza a variável "p1" (jogador 1) alterar a rodada
    - Utiliza a variável "p2" (jogador 2) alterar a rodada
    - Utiliza a variável "ver2" para identificar se o jogo anterior terminou em velha
    -------------------------------------------------------
    Retornos:
    - Retorna "matriz" como uma nova matriz
    - Retorna o novo valor de "rodada"
    '''
    matriz = inicializarTabuleiro()

    if (p1+p2)%2==0:
       if ver2=="end":
           rodada=1
       else:
           rodada=2

    else:
       if ver2=="end":
           rodada=2
       else:
           rodada=1

    return matriz,rodada

def programa():
    '''
    Função principal
    -------------------------------------------------------
    Parâmetros:
    - Não há parâmetros
    -------------------------------------------------------
    Retornos:
    - Não retorna valores
    '''
    #Variáveis
    p1 = 0
    p2 = 0
    rodada = 2

    #Controles bool
    jogos = True
    hub = True

    #Placar
    imprimePontuacao(p1,p2)

    #Inicializando tabuleiro
    matriz = inicializarTabuleiro()
    imprimirTabuleiro(matriz)

    #Programa
    while hub:
        r = imprimeMenuPrincipal()

        # Caso 1
        if r == 1:
            while p1 < 3 and p2 < 3:
                while jogos:
                    x, y = coordenadas()
                    jogadaUsuario(rodada, matriz, x, y)
                    ver = verificaVencedor(matriz)
                    ver2 = verificaVelha(matriz)
                    if ver == "end":
                        p1, p2 = mostraVencedor(rodada, p1, p2)
                        imprimePontuacao(p1, p2)
                        break
                    elif ver2 == "end":
                        imprimePontuacao(p1,p2)
                        break
                    else:
                        rodada += 1
                matriz, rodada = reset(matriz, rodada, p1, p2, ver2)

        # Caso 2
        elif r == 2:
            print("\nEssa função ainda está em desenvolvimento\n")

        # Caso 3
        elif r == 3:
            print("Programa Encerrado")
            hub = False

        # Caso Inválido
        else:
            print("\nOpção inválida\n")


programa()
