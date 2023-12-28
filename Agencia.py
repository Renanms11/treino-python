from Conta import Conta
class Agencia:

    _Banco = 'Banco novo'
    def __init__(self,numero,gerente, contas):
        self.numero = numero
        self.gerente = gerente
        self.contas = contas




    @classmethod
    def get_banco(cls):
        return cls._Banco

    @staticmethod
    def informacaoEmprestimo(valor,numeroParcelas):
        juros = valor * 0.20
        pagamentoParcelaunica = (valor+juros) -((valor+juros)*0.05)
        parcelas = (valor+juros)/numeroParcelas

        if numeroParcelas > 1:
            print(f'Emprestimo de {valor} será pago em {numeroParcelas}\n valor por parcela { parcelas} no valor total de'
                  f' R$ {parcelas*numeroParcelas}')
        else:
            print(f'Emprestimo de {valor} será pago em valor unico \n  valor R$ { pagamentoParcelaunica}')




    def OrdenarContas(self):
        for i in range(len(self.contas)-1):
            index =i
            for j in range(len(i+1,len(self.contas))):
                if self.contas[j]< self.contas[index]:
                    index = j


            aux =self.contas[i]
            self.contas[i] = self.contas[index]
            self.contas[index] = aux