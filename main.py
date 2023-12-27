from Conta import Conta


novaconta = Conta('1', '0138202074450','Renan miranda sena', 1000)

novaconta.depositar(300)

print(novaconta.saldo)

novaconta.retirada(1000)
print(novaconta.saldo)
novaconta.retirada(200)
print(novaconta.saldo)
novaconta.retirada(100)
print(novaconta.saldo)



