""" print("Brasil", "ganhou", 5, "titulos mundiais", sep="-")

print("çslkdjf", "çdf ", end="====")
 """
import random
def jogo_advinhacao():
    print("*********************************************")
    print("**********! Jogo da Advinhação !*************")
    print("*********************************************")
    num_secreto = random.randrange(1, 101) # pra n ser decimal
    print(num_secreto)
    #usando laco
    tentativas = 3
    pontos = 1000



    print("qual nivel de dificuldade ?")
    nivel = int(input(("digite (1)Facil (2)Medio (3)dificil: ")))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):# pq ele ignora o 5, 0 4
        print(f"tentativas: {rodada} de {tentativas}")
        chut = int(input("Digite um num de 1 e 100: "))
        print("voce digitou: ", chut)

        if chut < 1 or chut > 100:
            print(" vc deve digitar um num entre 1 e 100")
            continue
        acertou = chut == num_secreto
        maior = chut > num_secreto
        menor = chut < num_secreto

        if acertou:
            print("vc acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("vc errou! o seu chute foi maior")
            elif menor:
                print("vc errou! o seu chute foi menor!")
            pontos_pedidos = abs(num_secreto - chut)#pegar o num absoluto pra ignora val negativo
            pontos = pontos - pontos_pedidos
    print("fim do jogo")

    # gerar val random -> gerar val aleatorio
