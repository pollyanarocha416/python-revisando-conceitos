
import random

def jogo_forca():
    imprimir_mensagem_abertura()

    palavra_secreta = carregar_palavra_secreta()
    
    letras_acertadas = inicializar_palavra_acertadas(palavra_secreta)
    #print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    while(not enforcou and not acertou):     
        chute = pede_chute()
        
        if chute in palavra_secreta:
           marcar_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros+=1
            desenha_forca(erros)
        #erros igual a 6
        acertou = "_" not in letras_acertadas
        enforcou = erros == 7
        print(letras_acertadas)

    if acertou:
        imprimir_vencedor()
    else:
        imprimir_perdedor(palavra_secreta)
    

def imprimir_mensagem_abertura():
    print("*********************************************")
    print("**********! Jogo da Forca !*************")
    print("*********************************************")


def carregar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializar_palavra_acertadas(palavra):
    lista = ["_" for letra in palavra]
    return lista


def pede_chute():
    chute = str(input("Qual letra? "))
    chute = chute.strip().upper()
    return chute


def marcar_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
                    #print(f"encontrei a letra [{letra}] na posicao {index}")
        index += 1


def imprimir_vencedor():
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


def imprimir_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()




#execulta quando chamo diretamente
if __name__ == ("__main__"):
    jogo_forca()

# funcoes uteis:
#find() em q index esta o item passado
#endwith() o final do item termina com o q foi passado
#lower()
#tirar espaco em branco
#strip()