""" print("Brasil", "ganhou", 5, "titulos mundiais", sep="-")

print("çslkdjf", "çdf ", end="====")
 """
num_secreto = 42
#usando laco
tentativas = int(input("qtas tentativa vc quer ter? "))
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
        print("vc acertou")
        break
    else:
        if maior:
            print("vc errou! o seu chute foi maior")
        elif menor:
            print("vc errou! o seu chute foi menor!")

print("fim do jogo")
""" 
for rodar in range(1, 10, 2):# o 2 intercala
    print(rodar) """