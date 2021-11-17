from unittest import TestCase
from leilao.dominio import Usuario, Lance, Leilao

class TestLeilao(TestCase):

    def setUp(self):
        self.usuario1 = Usuario('usuario1')
        self.lance_do_usuario1 = Lance(self.usuario1, 100.00)

        self.leilao = Leilao('Objeto')  
    
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        usuario2 = Usuario('usuario2')
        lance_do_usuario2 = Lance(usuario2, 150.00)

        self.leilao.propoe(self.lance_do_usuario1)
        self.leilao.propoe(lance_do_usuario2)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado,  self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado,  self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(ValueError):
            usuario2 = Usuario('usuario2')
            lance_do_usuario2 = Lance(usuario2, 100.0)

            self.leilao.propoe(self.lance_do_usuario1)
            self.leilao.propoe(lance_do_usuario2)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):

        self.leilao.propoe( self.lance_do_usuario1)

        valor_esperado = 100.00

        self.assertEqual(valor_esperado,  self.leilao.menor_lance)
        self.assertEqual(valor_esperado,  self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        usuario2 = Usuario('usuario2')
        usuario3 = Usuario('usuario3')
        lance_do_usuario2 = Lance(usuario2, 150.00)
        lance_do_usuario3 = Lance(usuario3, 210.00)

        self.leilao.propoe(self.lance_do_usuario1)
        self.leilao.propoe(lance_do_usuario2)
        self.leilao.propoe(lance_do_usuario3)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 210.00

        self.assertEqual(menor_valor_esperado,  self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado,  self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_usuario1)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        usuario2 = Usuario('usuario2')
        lance_do_usuario2 = Lance(usuario2, 200.0)

        self.leilao.propoe(self.lance_do_usuario1)
        self.leilao.propoe(lance_do_usuario2)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebido)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance2_do_usuario1 = Lance(self.usuario1, 200.0)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_usuario1)
            self.leilao.propoe(lance2_do_usuario1)