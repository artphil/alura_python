class Programa:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor.title()

    def __str__(self):
        return f'Nome: {self.nome} ({self.ano})\nLikes: {self.likes}'
    
    def __repr__(self):
        return f'Programa(nome = {self.nome}, ano = {self.ano})'

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} ({self.ano})\nDuração: {self.duracao} min\nLikes: {self.likes}'

    def __repr__(self):
        return f'Filme(nome = {self.nome}, ano = {self.ano}, duracao = {self.duracao})'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} ({self.ano})\nTemporadas: {self.temporadas}\nLikes: {self.likes}'

    def __repr__(self):
        return f'Serie(nome = {self.nome}, ano = {self.ano}, temporadas = {self.temporadas})'

class Playlist:
    def __init__(self, nome, programas):
        self.__nome =  nome
        self.__listagem = programas
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor.title()

    def __getitem__(self, item):
        return self.__listagem[item]
    
    def __len__(self):
        return len(self.__listagem)


if __name__ == "__main__":
    vingadores =  Filme('vingadores - ultimato', 2018, 160)
    ddmatar =  Filme('duro de matar', 1988, 110)
    friends =  Serie('friends', 1999, 10)
    vingadores.dar_like()
    friends.dar_like()
    friends.dar_like()
    friends.dar_like()

    playlist = [vingadores, friends, ddmatar]
    minha_playlist = Playlist('minha playlist', playlist)

    print(len(minha_playlist))
    
    for programa in minha_playlist:
        print(programa)
