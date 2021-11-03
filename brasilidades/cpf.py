from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido.")

    def __str__(self):
        return self.formata_cpf()

    def valida_cpf(self, cpf):
        if len(cpf) != 11:
            raise ValueError("Quantidade de digitos inválida.")
        validador = CPF()
        return validador.validate(cpf)
    
    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
