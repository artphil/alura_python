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


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} ({self.ano})\nTemporadas: {self.temporadas}\nLikes: {self.likes}'


if __name__ == "__main__":
    vingadores =  Filme('vingadores - ultimato', 2018, 160)
    friends =  Serie('friends', 1999, 10)

    vingadores.dar_like()
    friends.dar_like()
    friends.dar_like()
    friends.dar_like()

    playlist = [vingadores, friends]
    for programa in playlist:
        print(programa)
