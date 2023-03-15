#string e url

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanatiza_url(url)
        self.valida_url()
    
    def sanatiza_url(self, url):
        return url.strip()
    
    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
    
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = url[:indice_interrogacao]
        return url_base
    
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros
    
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    
extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)








###############################################################
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
#sanatizacao da url
url = url.strip()# validacao da url
#n tem url
if url == "":
    raise ValueError("A URL está vazia")
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)#apartir de quantidade pra frente 
parametro_busca = 'quantidade'
#apartir de quantidade pra frente encontrar 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)# e a contagem disso daqui 'quantidade='
indice_valor = indice_parametro + len(parametro_busca) + 1
print(indice_valor)
# e pra encontrar isso daqui 'quantidade=100&'
indice_e_comercial = url_parametros.find('&', indice_valor)
print(indice_e_comercial)#14 # se vazio a busca comeca em '|quantidade=100 etc..'
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else: # se n for vazio o lop vai de quantidade=100
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)#              'quantidade=|100|'