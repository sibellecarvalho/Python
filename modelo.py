class Filme:
    def __init__(self, nome, ano, duracao) :
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

def dar_like(self):
    self.like += 1

class Serie:
    def __init__(self, nome, ano, temporada) :
        self.nome = nome.title()
        self.ano = ano
        self.temporada = temporada
        self.likes = 0

def dar_like(self):
    self.like += 1

vingadores = Filme ('vingadores - guerra infinita', 2018, 160)
print (f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
       f'- Duracao: {vingadores.duracao} - Likes: {vingadores.likes}')
vingadores.dar_like()

vincenzo = Serie('vincenzo', 2021, 1)

print (f'Nome: {vincenzo.nome} - Ano: {vincenzo.ano} '
       f'- Temporada: {vincenzo.temporada} - Likes: {vincenzo.likes}')
vincenzo.dar_like()
vincenzo.dar_like()
