arquivo_contatos = open('trabalhando com io/dados/contatos.csv', encoding='latin_1')

conteudo = arquivo_contatos.readlines()

for linha in conteudo:
    print(linha, end = '')
