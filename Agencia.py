from Conta import Conta
class Agencia:

    _Banco = 'Banco novo'
    def __init__(self,numero,gerente ,contas):
        self.numero=numero
        self.gerente = gerente
        self.contas = contas




    @classmethod
    def get_banco(cls):
        return cls._Banco


    def OrdenarContas(self):
        for i in range(len(self.contas)-1):
            index =i
            for j in range(len(i+1,len(self.contas))):
                if self.contas[j]< self.contas[index]:
                    index = j


            aux =self.contas[i]
            self.contas[i] = self.contas[index]
            self.contas[index] = aux