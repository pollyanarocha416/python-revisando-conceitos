# from fila_normal import fila_normal
from fila_prioritaria import FilaPrioritaria


""" fila_teste = fila_normal()
fila_teste.atualizafila()
fila_teste.atualizafila()
fila_teste.atualizafila()
fila_teste.atualizafila()
print(fila_teste.chamacliente(13))
print(fila_teste.chamacliente(1)) """
fila_teste_2 = FilaPrioritaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chama_cliente(20))
print(fila_teste_2.chama_cliente(2))
print(fila_teste_2.estatistica('10/01/1993', 12, 'detail'))
