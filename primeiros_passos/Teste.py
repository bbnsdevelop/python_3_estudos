numero = 2

for n in range(5):
   if n == 0:
       numero = numero * 1
   else:
       numero = numero * n

numero = 4 * ((numero / 2) + 1)
numero = numero + 0.25
print(numero)