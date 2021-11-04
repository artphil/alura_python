from cpf_cnpj import Documento


cpf = '015.  563.116-05'
cnpj = '03.778.130.0.001-48  '

objeto_cpf = Documento.cria_documento(cpf)
objeto_cnpj = Documento.cria_documento(cnpj)

print(objeto_cpf)
print(objeto_cnpj)

