
import random

def jogo_forca():
    imprimir_mensagem_abertura()

    palavra_secreta = carregar_palavra_secreta()
    
    letras_acertadas = inicializar_palavra_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        
        chute = str(input("Qual letra? "))
        chute = chute.strip().upper()
        
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                    print(f"encontrei a letra [{letra}] na posicao {index}")
                index+=1
        else:
            erros+=1
        #erros igual a 6
        acertou = "_" not in letras_acertadas
        enforcou = erros == 6
        print(letras_acertadas)
    if acertou:
        print("vc ganhou :)")
    else:
        print("vc perdeu :(")
    print("fim do jogo")


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









#execulta quando chamo diretamente
if __name__ == ("__main__"):
    jogo_forca()

# funcoes uteis:
#find() em q index esta o item passado
#endwith() o final do item termina com o q foi passado
#lower()
#tirar espaco em branco
#strip()