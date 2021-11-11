from datetime import datetime, timedelta

class DataBR:
    def __init__(self):
        pass
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format()
    
    def format(self):
        return self.momento_cadastro.strftime('%d/%m/%Y %H:%M')

    def mes_cadastro(self):
        lista_meses = [
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
        ]
        mes = self.momento_cadastro.month -1
        return lista_meses[mes]

    def dia_semana(self):
        lista_dias = [
            'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo'
        ]
        dia = self.momento_cadastro.weekday()
        return lista_dias[dia]

    def tempo_cadastro(self):
        agora = datetime.today()
        return agora - self.momento_cadastro