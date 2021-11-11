import requests

class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        cep = [d for d in cep if d.isdigit()]
        cep = ''.join(cep)
        if self.validate(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido.")

    def __str__(self):
        return self.format()

    def validate(self, cep):
        if len(cep) == 8:
            return True
        return False
    
    def format(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'

    def retorna_endereco(self): 
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )