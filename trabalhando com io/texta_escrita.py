arquivo_contatos = open(
    'trabalhando com io/dados/contatos-escrita.csv', encoding='latin_1', mode='w')

contatos = ['11,Carol,carol@carol.com.br\n',
            '12,Letícia,leticia@leticia.com.br\n',
            '13, Giulia,giulia@giulia.com.br\n',
            '15, Felipe,felipe@felipe.com.br\n']


for contato in contatos:
    arquivo_contatos.write(contato)

arquivo_contatos.flush()
input('Pressione <Enter> para encerrar o programa')