from cpf_cnpj import CpfCnpj


cpf = '015.563.116-05'
cnpj = '03.778.130.0.001-48  '

objeto_cpf = CpfCnpj(cpf, 'cpf')
objeto_cnpj = CpfCnpj(cnpj, 'cnpj')

# print(objeto_cpf)
print(objeto_cnpj)

