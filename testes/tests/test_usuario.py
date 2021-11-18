import pytest
from leilao.dominio import Usuario, Leilao
from leilao.excecoes import LanceInvalido

@pytest.fixture
def usuario1():
    return Usuario('usuario1', 100.0)

@pytest.fixture
def leilao():
    return Leilao('objeto')


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(usuario1, leilao):
   
    usuario1.propoe_lance(leilao, 50.0)

    assert usuario1.carteira == 50.00


def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(usuario1, leilao):

    usuario1.propoe_lance(leilao, 1.0)

    assert usuario1.carteira == 99.00


def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(usuario1, leilao):

    usuario1.propoe_lance(leilao, 100.0)

    assert usuario1.carteira == 0.0
 

def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(usuario1, leilao):
   
    with pytest.raises(LanceInvalido):

        usuario1.propoe_lance(leilao, 200.0)