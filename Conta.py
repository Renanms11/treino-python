import datetime

from Cliente import Cliente
from Extrato import  Extrato

class Conta:
    def __init__(self,clientes, cpf, numero,saldo):
        self.clientes= clientes
        self.cpf=cpf
        self.numero= numero
        self.saldo =saldo
        self.dataAbertura= datetime.datetime.today()
        self.extrato = Extrato()

    def  depositar (self,valor):
        self.saldo += valor
        self.extrato.transacoes.append(["Deposito",valor,'Data',datetime.datetime.today()])

    def  retirada(self,valor):
        if self.saldo > 0 and valor <= self.saldo:
            self.saldo -=valor
            self.extrato.transacoes.append(['Retirada',valor,'Data',datetime.datetime.today()])
            print('Retirada do valor de {}'.format(valor))
            #print(f'Retirada do Valor de {valor}')
            #print('Retirada do  valor de ' +  str(valor))
        else:
            print('Saldo insuficiente!')


    def transferencia(self, contaDestino, valor):
        if self.saldo >0 and self.saldo >= valor:
            self.saldo -=valor
            contaDestino.depositar(valor)
            self.extrato.transacoes.append(["Transferência",valor,'DAta',datetime.datetime.today()])

        else:
            return 'saldo insuficiente !'

