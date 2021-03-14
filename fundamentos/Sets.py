lista = ['11', 11, 11, 12, 1, 2, 3, 1, 2, 3, 'A', 'A', '1']


listSet = set(lista)

print(listSet)

conjuntoA = {1, 2, 3, 4, 4, 3}

print(conjuntoA)
print(listSet == conjuntoA)

conjuntoB = {2, 3, 1}
conjuntoC = {1, 2, 4}

print('união: ', conjuntoC.union(conjuntoB))
print('interseção: ', conjuntoC.intersection(conjuntoB))
conjuntoB.update(conjuntoC)
print('conjunto B', conjuntoB)
print('conjunto C', conjuntoC)
print(conjuntoC <= conjuntoB)
print('diferençao: ', conjuntoB - conjuntoC)
