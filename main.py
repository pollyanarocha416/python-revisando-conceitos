""" print("Brasil", "ganhou", 5, "titulos mundiais", sep="-")

print("çslkdjf", "çdf ", end="====")
 """
num_secreto = 42

rodada =1

#usando laco
tentativas = 5
while rodada < tentativas:
    print(f"tentativas: {rodada} de {tentativas}")
    chut = int(input("Digite seu num: "))
    print("voce digitou: ", chut)

    acertou = chut == num_secreto
    maior = chut > num_secreto
    menor = chut < num_secreto

    if acertou:
        print("vc acertou")
    
    else:
        if maior:
            print("vc errou! o seu chute foi maior")
        elif menor:
            print("vc errou! o seu chute foi menor!")
    rodada = rodada +1
print("fim do jogo")    