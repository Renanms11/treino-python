from Conta import Conta
import datetime

class ContaEspecial(Conta):

    def __init__(self,cliente,numero,saldo,limite):
        Conta.__init__(self,cliente,numero,saldo)
        self.limite = limite
    def retirada(self,valor):
        if(self.saldo + self.limite )< valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes("Sacar",valor,'Data',datetime.datetime.today())
            return  True


