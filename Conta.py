from Cliente import Cliente

class Conta:
    def __init__(self,clientes, cpf, titular,saldo):
        self.clientes= clientes
        self.cpf=cpf
        self.titular= titular
        self.saldo =saldo

    def  depositar (self,valor):
        self.saldo += valor

    def  retirada(self,valor):
        if self.saldo > 0 and valor <= self.saldo:
            self.saldo -=valor
            print('Retirada do valor de {}'.format(valor))
            #print(f'Retirada do Valor de {valor}')
            #print('Retirada do  valor de ' +  str(valor))
        else:
            print('Saldo insuficiente!')


    def transferencia(self, contaDestino, valor):
        if self.saldo >0 and self.saldo >= valor:
            self.saldo -=valor
            contaDestino.depositar(valor)

        else:
            return 'saldo insuficiente !'
