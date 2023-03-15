#herdar de mais de uma class


class Funcionario:

    def registra_horas(self, horas):
        print('Horas registradas...')
    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')
    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!') 
    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Junior(Alura, Caelum):
    pass 

class Pleno(Alura, Caelum):
    pass


jose = Junior()
jose.busca_perguntas_sem_resposta()
jose.busca_cursos_do_mes()
'''
Avancando em OOP, oop pt2
'''
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    @property
    def likes(self):
        return self._likes
    def dar_like(self):
        self._likes += 1
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
         self._nome = novo_nome.title()
    def __str__(self):
        return f'Programa: {self._nome} - {self.ano} - Likes: {self._likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'Programa: {self._nome} - {self.duracao} min - lancamento {self.ano} - Likes: {self._likes}'
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    def __str__(self):
        return f'Programa: {self._nome} - {self.temporadas} temporada(s) - lancamento {self.ano} - Likes: {self._likes}'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
#tornar a class iteravel/itereb
    def __getitem__(self, item):
        return self._programas[item]
    @property
    def listagem(self):
        return self._programas
    def __len__(self):
        return len(self._programas)
vingadores = Filme('vingadores guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 2000, 100)
demolidor = Serie('demolidor', 2016, 2)
vingadores.dar_like()
tmep.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
tmep.dar_like()
demolidor.dar_like()
filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)
#O porlimorfismo acontece aqui
#pq nao importa quem será imprimido
#esse imprime e polimorfico print('tamanho', len(playlist_fim_de_semana))
for programa in playlist_fim_de_semana:
    print(programa)
    print('ta ou nao ta? ', demolidor in playlist_fim_de_semana)
