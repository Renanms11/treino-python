import math


class ExcecaoCustomizada(Exception):
    def __init__(self, texto ,valor ):
        super().__init__(texto, valor)
        self._valor = valor

    @property
    def valor(self):
        return  self._valor


    def __str__(self):
        return f'{self.args[0]} -> {self._valor}'
