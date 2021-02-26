class Conta:
	def __init__(self, numero, titular, saldo, limite):
		self.numero = numero
		self.titular = titular
		self.saldo = saldo
		self.limite = limite

	def deposita(self, valor):
		self.saldo += valor

	def saca(self, valor):
		self.saldo -= valor

	def extrato(self):
		print("numero:	{}	\nsaldo:	{}".format(self.numero, self.saldo))


conta = Conta('123-4', 'João', 120.0, 1000.0)

conta.deposita(20.0)
conta.extrato()
# numero:	'123-4'
# saldo:	140.0
conta.saca(15)
conta.extrato()
