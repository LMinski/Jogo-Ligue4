#Jogo Ligue4

import os

num_coluna = 7
num_linha = 6
matriz = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]


def mostraTabuleiro(tab):
    #Essa função separa os elementos em formato de tabela e corta os elementos 
    for l in tab:
        print('           |', end='')
        for c in l:
            print (f'{c} |', end= '')
        print()

def inputPonto(col,jogador):
    #Essa função imprime os movimentos e contabiliza os mesmos.
    col = col - 1
    for l in range(num_linha-1, -1, -1):
        if matriz[l][col] == 0:
            matriz[l][col]=jogador
            break 

def diagonal():
    #Detecta vitória para diagonais no sentido esquerda pra direita, de baixo para cima.
    for l in range (3, num_linha):
        for col in range(0, 4):
            if matriz[l][col] > 0:
                if matriz[l][col] == matriz[l - 1][col + 1] == matriz[l - 2][col + 2] == matriz[l - 3][col + 3]:
                    if matriz[l][col] == 1:
                        print(f'            Jogador 1  Vencedor!')
                    else: 
                        print(f'            Jogador 2  Vencedor!')
                    return True
    
    #Detecta vitória para diagonais no sentido esquerda para direita, de cima para  baixo.
    for l in range (0, 3):
        for col in range(0, 4):
            if matriz[l][col] > 0:
                if matriz[l][col] == matriz[l + 1][col + 1] == matriz[l + 2][col + 2] == matriz[l + 3][col + 3]:
                    if matriz[l][col] == 1:
                        print(f'            Jogador 1  Vencedor!')
                    else: 
                        print(f'            Jogador 2  Vencedor!')
                    return True


def horizontal():
    #Detecta vitória na horizontal.
    for l in range(0, num_linha):
        for col in range(0,4):
            if matriz[l][col] > 0:
                if matriz[l][col] == matriz[l][col+1] == matriz[l][col + 2] == matriz[l][col + 3]:
                    if matriz[l][col] == 1:
                        print(f'            Jogador 1  Vencedor!')
                    else: 
                        print(f'            Jogador 2  Vencedor!')
                    return True 
    
def vertical():
    #Detecta vitória na vertical.
    for l in range(0, 3):
        for col in range(0, num_coluna):
            if matriz[l][col] > 0:
                if matriz[l][col] == matriz[l + 1][col] == matriz[l + 2][col] == matriz[l + 3][col]:
                    if matriz[l][col] == 1:
                        print(f'            Jogador 1  Vencedor!')
                    else: 
                        print(f'            Jogador 2  Vencedor!')
                    return True



def vitoria():
    #função para quebrar o while e encerrar o jogo.
    if diagonal() or horizontal() or vertical():
        return True

mostraTabuleiro(matriz)
while not vitoria():
    #Estrutura de repetição para contabilizar jogadas e dar input nos pontos dados na matriz.
    Jogador1 = int(input('Jogador 1 -> Selecione uma coluna de 1 a 7: '))
    if Jogador1 > 7 or Jogador1 < 1:
        while Jogador1 > 7 or Jogador1 < 1:
            Jogador1 = int(input('Você selecionou uma coluna fora do limite! Selecione uma coluna de 1 a 7: '))
    os.system('cls')
    inputPonto(Jogador1, 1)
    mostraTabuleiro(matriz)
    if vitoria() == True: 
        break
    Jogador2 = int(input('Jogador 2 -> Selecione uma coluna de 1 a 7: '))
    if Jogador2 > 7 or Jogador2 < 1:
        while Jogador2 > 7 or Jogador2 < 1:
            Jogador2 = int(input('Você selecionou uma coluna fora do limite! Selecione uma coluna de 1 a 7: '))
    os.system('cls')
    inputPonto(Jogador2, 2)
    mostraTabuleiro(matriz)
    
