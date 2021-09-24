import re


class ExtratorURL:
    def __init__(self, url):
        """Salva a url em um atributo do objeto (self.url = url) e verifica se a url é válida"""
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.url)
    
    def __str__(self):
            return f'{self.url}\nBase: {self.get_url_base()}\nParâmetros: {self.get_url_parametros()}'

    def __eq__(self, other):
        return self.url == other.url

    def sanitiza_url(self, url):
        """Retorna a url removendo espaços em branco."""
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        """Valida se a url está vazia"""
        if not self.url:
            raise ValueError("A url não pode estar vazia.")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        """Retorna a base da url."""
        indice_interrogacao  = self.url.find('?')
        return self.url[:indice_interrogacao ]

    def get_url_parametros(self):
        """Retorna os parâmetros da url."""
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        """Retorna o valor do parametro `parametro_busca`."""
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
        


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)
print("O tamanho da URL é: ", len(extrator_url))
print("URL completa: ", extrator_url)
print("extrator_url == extrator_url_2? ", extrator_url == extrator_url_2)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print("Valor do parâmetro 'quantidade': ", valor_quantidade)


VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = float(extrator_url.get_valor_parametro("quantidade"))


if(moeda_origem == 'dolar'):
    novaQuantidade = quantidade * VALOR_DOLAR
else:
    novaQuantidade = float(quantidade) / VALOR_DOLAR

print(f'{quantidade:.2f} de {moeda_origem} equivalem à {novaQuantidade:.2f} de {moeda_destino}.') 
