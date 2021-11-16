from unittest import TestCase
from leilao.dominio import Usuario, Lance, Leilao

class TestLeilao(TestCase):

    def setUp(self):
        self.usuario1 = Usuario('usuario1')
        self.lance_do_usuario1 = Lance(self.usuario1, 100.00)

        self.leilao = Leilao('Objeto')  
    
    def test_avalia_lance_ordem_crescente(self):
        self.usuario2 = Usuario('usuario2')
        self.lance_do_usuario2 = Lance(self.usuario2, 150.00)

        self.leilao.propoe(self.lance_do_usuario1)
        self.leilao.propoe(self.lance_do_usuario2)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado,  self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado,  self.leilao.maior_lance)

    def test_avalia_lance_ordem_decrescente(self):
        self.usuario2 = Usuario('usuario2')
        self.lance_do_usuario2 = Lance(self.usuario2, 150.00)

        self.leilao.propoe(self.lance_do_usuario2)
        self.leilao.propoe(self.lance_do_usuario1)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado,  self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado,  self.leilao.maior_lance)

    def test_avalia_lance_unico(self):

        self.leilao.propoe( self.lance_do_usuario1)

        valor_esperado = 100.00

        self.assertEqual(valor_esperado,  self.leilao.menor_lance)
        self.assertEqual(valor_esperado,  self.leilao.maior_lance)

    def test_avalia_tres_lances(self):
        self.usuario2 = Usuario('usuario2')
        self.usuario3 = Usuario('usuario3')
        self.lance_do_usuario2 = Lance(self.usuario2, 150.00)
        self.lance_do_usuario3 = Lance(self.usuario3, 110.00)

        self.leilao.propoe(self.lance_do_usuario1)
        self.leilao.propoe(self.lance_do_usuario2)
        self.leilao.propoe(self.lance_do_usuario3)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado,  self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado,  self.leilao.maior_lance)