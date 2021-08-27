

class Conta:
    def __init__(self, numero, titular, saldo=0.0, limite=1000.0):
        self.__numero = numero
        self.__titular = titular.title()
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, valor):
        self.__saldo += valor 

    def __pode_sacar(self, valor):
        return valor <= (self.__saldo + self.__limite)

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            return True 
        else:
            print(f'O valor {valor} esta acima do disponível.')
            return False 
    
    def transfere(self, valor, destino):
        if (self.saca(valor)):
            destino.deposita(valor)

    def extrato(self):
        print(f'O saldo de {self.__titular} é: {self.__saldo}\nO valor disponível é: {self.__saldo + self.__limite}')
    
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor
    
    @staticmethod
    def codigo_banco():
        return '001'
