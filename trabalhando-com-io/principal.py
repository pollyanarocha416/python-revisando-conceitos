import contatos_utils
try:
    contatos = contatos_utils.csv_para_contatos('trabalhando-com-io/dados/contatos.csv')
    for contato in contatos:
        print(f"{contato.id} - {contato.nome} - {contato.email}")

except FileNotFoundError:
    print('Arquivo nao encontrado')
except PermissionError:
    print('Sem permicao de escrita')


