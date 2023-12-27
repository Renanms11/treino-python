from Conta import Conta
from Cliente import Cliente
from Extrato import Extrato

cliente1 = Cliente('01382074450','renan miranda sena','rua alameda das mansoes')
cliente2 = Cliente('06125661377','katianny maia','rua alamenda das mansoes')



novaconta = Conta([cliente1,cliente2], '0138202074450',1, 2000)

novaconta.depositar(1500)
novaconta.retirada(999)
novaconta.extrato .extrato(1)






