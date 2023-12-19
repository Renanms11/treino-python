
def ordenarListaNumero(listas):
    auxiliar = 0
    tamanhoLista= len(listas)
    for i in range(tamanhoLista -1):
        for ii in range(tamanhoLista-1):
            if listas[ii] > listas[ii+1]:
                auxiliar = listas[ii+1]
                listas[ii+1] = listas[ii]
                listas[ii] = auxiliar

def inverterString(texto):
    arrayChar = len(texto)
    listaTexto = list(texto)

    for i in range(arrayChar // 2):
        aux = listaTexto[i]
        listaTexto[i] = listaTexto[arrayChar - 1 - i]
        listaTexto[arrayChar - 1 -i] = aux
        texto = ''.join(listaTexto)

    return texto




texto = input("digite seu nome completo :")
texto =inverterString(texto)
print(texto)




