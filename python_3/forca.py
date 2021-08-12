import random

def jogar():
    imprime_cabecalho()
    palavra_secreta, letras_acertadas = escolhe_palavra()

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 6

    print('Palavra:', *letras_acertadas)

    while(not enforcou and not acertou):

        print('Tentaticas restantes:', tentativas-erros)
        chute = le_chute()

        if (chute in palavra_secreta):
           registra_chute(chute, palavra_secreta,letras_acertadas)
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

def imprime_cabecalho():
    print('###########################################')
    print('############# Jogo da Forca ###############')
    print('###########################################')

def escolhe_palavra():
    palavra_secreta = ''

    with open('palavras.txt', 'r', encoding='utf8') as file:
        palavras = file.readlines()
        palavra_secreta = palavras[random.randrange(len(palavras))]
        palavra_secreta = palavra_secreta.strip()
        palavra_secreta = palavra_secreta.upper()

    letras_acertadas = ['_' for l in palavra_secreta]
    
    return palavra_secreta, letras_acertadas

def le_chute()
    chute = input('Qual a letra? ')
    chute = chute.strip()
    chute = chute.upper()
    return chute

def registra_chute(chute, palavra_secreta,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (letra == chute):
            letras_acertadas[index] = letra
        index += 1


if (__name__ == "__main__"):
    jogar()