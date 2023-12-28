import math


class ExcecaoCustomizada(Exception):
    pass
 # exemplo pego um faunção escrita por min e boto aqui em baixo
    def calcularSqrt(x):
        if a < 0:
            #aqui pode se impremir oque quiser
            raise ExcecaoCustomizada("Ovalor fornecido e menor que zero")
        return math.sqrt(x)
