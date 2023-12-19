
def ordenarListaNumero(listas):
    auxiliar = 0
    tamanhoLista= len(lista)
    for i in range(tamanhoLista -1):
        for ii in range(tamanhoLista-1):
            if lista[ii] > lista[ii+1]:
                auxiliar = lista[ii+1]
                lista[ii+1] = lista[ii]
                lista[ii] = auxiliar




lista =[10,5,8,4,6,1,3,11,14,0,2]



ordenarListaNumero(lista)

print(lista)


