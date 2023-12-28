from Conta import Conta
from Poupança import Poupança

class contaRemuneradaPoupança(Conta,Poupança):
    def __init__(self ,cliente,numero,saldo,taxadeRemuneraçao):
        Conta.__init__(self,cliente,numero,saldo,)
        Poupança.__init__(self,Poupança)

