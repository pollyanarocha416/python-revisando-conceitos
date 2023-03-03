import forca
import jogoAdivinhacao


print("*********************************************")
print("**********! Escolha seu jogo !*************")
print("*********************************************")

print("(1)Forca (2)Adivinhacao")
jogo = int(input("Qual jogo? "))

if jogo == 1:
    print("Jogando forca")
    forca.jogo_forca()
else:
    print("Jogando advinhacao")
    jogoAdivinhacao.jogo_advinhacao()
    
