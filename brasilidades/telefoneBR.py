import re

class TelefoneBR:
    def __init__(self, telefone):
        telefone = str(telefone)
        telefone = [d for d in telefone if d.isdigit()]
        telefone = ''.join(telefone)
        if self.validate(telefone):
            self.numero = telefone
        else:
            raise ValueError("Telefone inválido.")

    def __str__(self):
        return self.format()

    def validate(self, telefone):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.search(padrao,telefone)
        if resposta:
            self.grupos = resposta.groups()
            return True
        return False
    
    def format(self):
        return '+{} ({}) {}-{}'.format(*self.grupos)