def selectiveSort(lista):

    posicao =0
    for  i in range(len(lista )):
        menor =i

        for j in range(i+1, len(lista)):
            if lista[j]< lista[menor]:
                menor = j

        # Se o elemento atual não é o menor, troca-os
        if lista[i] != lista[menor]:
            aux = lista[i]
            lista[i] = lista[menor]
            lista[menor] = aux



lista = [10,5,9,1,3,4,6,2,7,5,8]
selectiveSort(lista)

for x in lista:
    print(x , end = " ")




