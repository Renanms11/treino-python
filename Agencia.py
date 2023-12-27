from Conta import Conta
class Agencia:

    def __init__(self,numero,gerente ,contas):
        self.numero=numero
        self.gerente = gerente
        self.contas = contas









    def OrdenarContas(self):
        for i in range(len(self.contas)-1):
            index =i
            for j in range(len(i+1,self.contas)):
                if self.contas[j]< self.contas[index]:
                    index = j


            aux =self.contas[i]
            self.contas[i] = self.contas[index]
            self.contas[index] = aux