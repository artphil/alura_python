import random

def jogar():
    print('###########################################')
    print('############# Jogo da Forca ###############')
    print('###########################################')

    palavra_secreta = ''

    with open('palavras.txt', 'r', encoding='utf8') as file:
        palavras = file.readlines()
        palavra_secreta = palavras[random.randrange(len(palavras))]
        palavra_secreta = palavra_secreta.strip('\n')
        palavra_secreta = palavra_secreta.upper()

    letras_acertadas = ['_' for l in palavra_secreta]

    enforcou = False
    acertou = False

    erros = 0
    tentativas = 6

    print('Palavra:', *letras_acertadas)

    while(not enforcou and not acertou):

        print('Tentaticas restantes:', tentativas-erros)
        chute = input('Qual a letra? ')
        chute = chute.strip()
        chute = chute.upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (letra == chute):
                    letras_acertadas[index] = letra

                index += 1


        else:
            erros += 1
    
        enforcou = erros == tentativas
        acertou = "_" not in letras_acertadas

        print('Palavra:', *letras_acertadas)


    if (acertou):
        print('\nVocê ganhou!!\n')
    else:
        print('\nVocê perdeu. :(\n')
            
    print('Fim do jogo.')

if (__name__ == "__main__"):
    jogar()