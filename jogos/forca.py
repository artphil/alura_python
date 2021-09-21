import random

def jogar():
    imprime_cabecalho()

    palavra_secreta, letras_acertadas = escolhe_palavra()
    print('Palavra:', *letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 7
    chutes_anteriores = []


    while(not enforcou and not acertou):

        print('Tentaticas restantes:', tentativas-erros)
        chute = le_chute()

        if (chute in chutes_anteriores):
            print(f'A letra {chute} já foi registrada.\nTente novamente')
        else:
            chutes_anteriores.append(chute)
            if (chute in palavra_secreta):
               registra_chute(chute, palavra_secreta,letras_acertadas)
            else:
                erros += 1
                desenha_forca(erros)

        enforcou = erros == tentativas
        acertou = "_" not in letras_acertadas

        print('Palavra:', *letras_acertadas)


    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
            
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

def le_chute():
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

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros >= 1):
        print(" |      (_)   ")
    
    if(erros >= 4):
        print(" |      \|/   ")
    elif(erros >= 3):
        print(" |      \|    ")
    elif(erros >= 2):
        print(" |       |    ")
    else:
        print(" |            ")

    if(erros >= 5):
        print(" |       |    ")
    else:
        print(" |            ")

    if (erros >= 7):
        print(" |      / \   ")
    elif(erros >= 6):
        print(" |      /     ")
    else:
        print(" |            ")


    print(" |            ")
    print("_|___         ")
    print()

    
if (__name__ == "__main__"):
    jogar()