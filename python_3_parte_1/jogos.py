import advinhacao
import forca

def escolhe_jogo():
    print('Escolha o jogo que deseja jogar:')
    print('(1) Adivinhação (2) Forca (0) Sair')

    return int(input('Defina o jogo: '))

print('###########################################')
print('############# Jogos Simples ###############')
print('###########################################')

jogo = escolhe_jogo()

while jogo > 0:
    if(jogo == 1):
        advinhacao.jogar()
    elif(jogo == 2):
        forca.jogar()

    jogo = escolhe_jogo()

print('Fim do programa.')

