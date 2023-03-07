

def jogo_forca():
    print("*********************************************")
    print("**********! Jogo da Forca !*************")
    print("*********************************************")


    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

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
#execulta quando chamo diretamente
if __name__ == ("__main__"):
    jogo_forca()

# funcoes uteis:
#find() em q index esta o item passado
#endwith() o final do item termina com o q foi passado
#lower()
#tirar espaco em branco
#strip()