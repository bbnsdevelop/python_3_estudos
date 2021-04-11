myFile = open('fundamentos/files/texto.txt')

print(myFile.readline())
myFile.seek(0) # reseta a leitura e volta para o inicio
print(myFile.read())
myFile.seek(0)
print('***************inicio*do*for******************')
for line in myFile:
    print(line)