minhaList = [1,2,3,4]

print(minhaList)

minhaList.extend([5, 9,7, 'A', 'teste', 'C', 'B', 'A'])

print(minhaList)
print(minhaList.pop()) # ultimo elemento

print(minhaList)

print(minhaList.pop(0)) #indice zero

minhaList.sort() # ordena

print(minhaList)

matriz = [[1,2,3],[7,8,9],[4,5,6]]

print(matriz)

print(matriz[1][1]) # exibi o 8

#compressao de lista
outraLista = [row[0] for row in matriz]

print(outraLista)



minhaLista = [1,2,3]
for i in minhaList:
    print(i)