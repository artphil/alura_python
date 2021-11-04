from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        documento = [d for d in documento if d.isdigit()]
        documento = ''.join(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de digitos inválida.")

class DocCpf:
    def __init__(self, documento):
        if self.validate(documento):
            self.documento = documento
        else:
            raise ValueError("CPF inválido.")

    def __str__(self):
        return self.format()

    def validate(self, documento):
        validador = CPF()
        return validador.validate(documento)
    
    def format(self):
        mascara = CPF()
        return mascara.mask(self.documento)


class DocCnpj:
    def __init__(self, documento):
        if self.validate(documento):
            self.documento = documento
        else:
            raise ValueError("CNPJ inválido.")

    def __str__(self):
        return self.format()


    def validate(self, documento):
        validador = CNPJ()
        return validador.validate(documento)
    
    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.documento)
