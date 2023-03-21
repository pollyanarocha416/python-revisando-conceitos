# from fila_normal import fila_normal
""" from fila_prioritaria import FilaPrioritaria """
from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
# from estatistica_resumida import EstatisticaResumida


""" fila_teste = fila_normal()
fila_teste.atualizafila()
fila_teste.atualizafila()
fila_teste.atualizafila()
fila_teste.atualizafila()
print(fila_teste.chamacliente(13))
print(fila_teste.chamacliente(1)) """
""" fila_teste_2 = FilaPrioritaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chama_cliente(20))
print(fila_teste_2.chama_cliente(2))
print(fila_teste_2.estatistica('10/01/1993', 12, 'detail'))
 """
teste_fabrica = FabricaFila.pega_fila('prioritaria')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(2))
print(teste_fabrica.estatistica(EstatisticaDetalhada('21/03/2023', 120)))
