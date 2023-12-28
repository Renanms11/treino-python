import math
from MinhaException import ExcecaoCustomizada
import numpy as np
from tkinter import *

'''

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text= "essa é minha primeira janela Python !!!!! Hello world !")

janelaPrincipal.geometry('500x500')
texto.pack()
janelaPrincipal.mainloop()


matriz1=np.array([[1,2],[3,4],[5,6]])
matriz2=np.array([[7,8],[9,10],[11,12]])
matriz2=matriz1+matriz2
print(matriz2)
matriz2=matriz2-matriz1
print(matriz2)

for indice,valor in enumerate(matriz):
    print(matriz[indice][indice]) '''

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(matriz)):
        print(matriz[i][i] , end = ' ')

#implementando minha exception Personalizada
def calcularSqrt(x):
    if x <0:
        raise ExcecaoCustomizada("minha excepao personaliza",x)
    else:
        return math.sqrt(x)