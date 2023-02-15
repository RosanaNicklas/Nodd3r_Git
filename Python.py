
# lista vacia para invertir la lista inicial
A1=[]
# el último valor (index -1)
i=-1
# revertimos el orden de la lista inicial (A)
while len(A1)<len(A):
A1.append(A[i])
i-=1 # i = i-1
A1





# palíndromo o no
different = 0 # inicializamos la variable
for i in range(len(A)):
if A[i] != A1[i]:
different += 1
if different == 0:
print("palíndromo")
else:
print("no un palíndromo")
print("tenemos", different, "elementos diferentes")