class IteradorHttp():
    def __init__(self, path):
        self.registro = open(path, 'r')
        self.linha_atual = ''
    def __iter__(self):
        return self
    def __next__(self):
        self.linha_atual = self.registro.readline()
        while self.linha_atual and not self.linha_atual.startswith('http://'):
            self.linha_atual = self.registro.readline()
        if self.linha_atual:
            return self.linha_atual
        raise StopIteration

class Iterador2Http():
    def __init__(self, path):
        self.registro = open(path, 'r')

    def iterator(self):
        for linha_atual in self.registro.readlines():
            if not linha_atual.startswith('http'):
                yield linha_atual

    

# iterador = IteradorHttp('craft-popular-urls.txt')
iterador = Iterador2Http('craft-popular-urls.txt')

for url in iterador.iterator():
    print(url)