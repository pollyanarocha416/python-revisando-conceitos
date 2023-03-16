arquivos1 = open('trabalhando com io/dados/contatos-escrita.csv', encoding='latin_1', mode='w')
arquivos2 = open('trabalhando com io/dados/contatos-escrita.csv',
                 encoding='latin_1', mode='a')

contato_carol = '11,Carol,carol@carol.com.br\n'
contato_andreza = '12,Adreza,andreza@andreza.com.br\n'

arquivos1.write(contato_carol)
arquivos2.write(contato_andreza)

arquivos1.close()
arquivos2.close()