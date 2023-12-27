import datetime

from Cliente import Cliente
from Extrato import  Extrato

class Conta:
    def __init__(self,clientes, cpf, numero,saldo):
        self.__clientes= clientes
        self.__cpf=cpf
        self.__numero= numero
        self.__saldo = saldo
        self.__dataAbertura= datetime.datetime.today()
        self.extrato = Extrato()

    @property
    def Saldo(self):
        return self.__saldo

    @Saldo.setter
    def Saldo(self,saldo):
        if self.__saldosaldo< 0 :
            print("saldo inválido")
        else:
            self.__saldo =saldo


    @property
    def Cliente(self):
        return self.__clientes



    def  depositar (self,valor):
        self.__saldo += valor
        self.extrato.transacoes.append(["Deposito",valor,'Data',datetime.datetime.today()])

    def  retirada(self,valor):
        if self.__saldo > 0 and valor <= self.__saldo:
            self.__saldo -=valor
            self.extrato.transacoes.append(['Retirada',valor,'Data',datetime.datetime.today()])
            print('Retirada do valor de {}'.format(valor))
            #print(f'Retirada do Valor de {valor}')
            #print('Retirada do  valor de ' +  str(valor))
        else:
            print('Saldo insuficiente!')


    def transferencia(self, contaDestino, valor):
        if self.__saldo >0 and self.__saldo >= valor:
            self.__saldo -=valor
            contaDestino.depositar(valor)
            self.extrato.transacoes.append(["Transferência",valor,'DAta',datetime.datetime.today()])

        else:
            return 'saldo insuficiente !'

