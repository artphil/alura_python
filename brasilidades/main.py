from cpf_cnpj import Documento
from telefone_br import TelefoneBR
from data_br import DataBR
from acesso_cep import BuscaEndereco

cpf = '015.  563.116-05'
cnpj = '03.778.130.0.001-48  '

objeto_cpf = Documento.cria_documento(cpf)
objeto_cnpj = Documento.cria_documento(cnpj)

print(objeto_cpf)
print(objeto_cnpj)

telefone = '+55 31 999999999'

objeto_telefone = TelefoneBR(telefone)

print(objeto_telefone)

hoje = DataBR()

print(hoje)
print(hoje.mes_cadastro())
print(hoje.dia_semana())

cep = '30270450'

objeto_cep = BuscaEndereco(cep)

print(objeto_cep)
print(*objeto_cep.acessa_via_cep())