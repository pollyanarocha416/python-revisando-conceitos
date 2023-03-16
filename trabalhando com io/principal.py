try:
    arquivo_contatos = open('trabalhando com io/dados/contatos.csv', encoding='latin_1')

    for linha in arquivo_contatos:
        print(linha, end='')
finally:
    arquivo_contatos.close()