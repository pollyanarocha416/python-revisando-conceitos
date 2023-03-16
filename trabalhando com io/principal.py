try:
    with open('trabalhando com io/dados/contatos.csv', encoding='latin_1') as arquivo_contatos:

        for linha in arquivo_contatos:
            print(linha, end='')
except FileNotFoundError:
    print('Arquivo nao encontrado')
except PermissionError:
    print('Sem permicao de escrita')

