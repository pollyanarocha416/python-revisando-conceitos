
contato_carol = '11,Carol,carol@carol.com.br\n'
contato_andreza = '12,Adreza,andreza@andreza.com.br\n'

with open('trabalhando com io/dados/contatos-escrita.csv', encoding='latin_1', mode='w') as arquivos1:
    arquivos1.write(contato_carol)
with open('trabalhando com io/dados/contatos-escrita.csv', encoding='latin_1', mode='a') as arquivos2:
    arquivos2.write(contato_andreza)
