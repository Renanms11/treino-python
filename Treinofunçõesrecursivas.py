# outra forma de importar conteudo
#import tkinter
#import tkinter as tk


from tkinter import *

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal , text= 'minha janela')
janelaPrincipal.title('Minha janela')
texto.place(x = 300 , y = 450)

janelaPrincipal.mainloop()

