

def jogo_forca():
    print("*********************************************")
    print("**********! Jogo da Forca !*************")
    print("*********************************************")
    print("fim do jogo")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    index = 0
    while(not enforcou and not acertou):
        chute = str(input("Qual letra? "))
        chute = chute.strip()
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print(f"encontrei a letra [{letra}] na posicao {index}")
            index = index +1

#execulta quando chamo diretamente
if __name__ == ("__main__"):
    jogo_forca()


# funcoes uteis:
#find() em q index esta o item passado
#endwith() o final do item termina com o q foi passado
#lower()
#tirar espaco em branco
#strip()