from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        documento = str(documento)
        doclist = [d for d in documento if d.isdigit()]
        documento = ''.join(doclist)
        self.tipo_documento = tipo_documento
        if tipo_documento == 'cpf':
            if self.valida_cpf(documento):
                self.documento = documento
            else:
                raise ValueError("CPF inválido.")
        if tipo_documento == 'cnpj':
            if self.valida_cnpj(documento):
                self.documento = documento
            else:
                raise ValueError("CNPJ inválido.")

    def __str__(self):
        if self.tipo_documento == 'cpf':
            return self.formata_cpf()
        if self.tipo_documento == 'cnpj':
            return self.formata_cnpj()

    def valida_cpf(self, cpf):
        if len(cpf) != 11:
            raise ValueError("Quantidade de digitos inválida.")
        validador = CPF()
        return validador.validate(cpf)
    
    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.documento)

    def valida_cnpj(self, cnpj):
        if len(cnpj) != 14:
            raise ValueError("Quantidade de digitos inválida.")
        validador = CNPJ()
        return validador.validate(cnpj)
    
    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.documento)
