import random

def jogar():
    print('###########################################')
    print('######### Adivinhe o número ###############')
    print('###########################################')

    numero_secreto = random.randrange(0,101)
    total_de_tentativas = 0
    pontos = 1000

    print('Escolha o nível de dificuldade:')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível: '))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f'\nTentativa {rodada} de {total_de_tentativas}')
        
        chute = int(input('Digite um número entre 1 e 100: '))
        
        if (chute < 1 or chute > 100):
            print('VocÊ deve digitar um número entre 1 e 100.')
            continue

        acertou = chute == numero_secreto 
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print(f'Você acertou e fez {pontos} pontos.')
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos
            if(maior):
                print('Seu chute foi maior que o número secreto.')
            elif (menor):
                print('Seu chute foi menor que o número secreto.')

            if (rodada == total_de_tentativas):
                print(f'O número secreto era {numero_secreto}.')

    print('Fim do jogo.')

if (__name__ == "__main__"):
    jogar()