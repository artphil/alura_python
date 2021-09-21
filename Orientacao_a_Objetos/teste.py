from conta import Conta


print(Conta.codigo_banco())

c1 = Conta(132,'marco antonio')
c1.extrato()
c1.deposita(400)
c1.extrato()
c1.saca(600)
c1.extrato()
c1.saca(1000)
c1.extrato()

print(c1.limite)

c2 = Conta(123,'HUGO REIS',30,2000)
c2.extrato()

c1.transfere(100, c2)
c1.extrato()
c2.extrato()
