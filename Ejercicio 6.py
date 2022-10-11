#Leer un vector X de N componentes y un número A y buscar si A es igual a algún elemento del
#vector X. Imprimir la o las posiciones donde se encontraron y si no encuentra ningún valor
#igual a A, entonces emitir un mensaje que lo indique.

vector=[]
for i in range (0,int(input("Inserte numero de componentes distintos de 0 "))):
    vector.append(int(input("Inserte componente ")))
a=int(input("Inserte numero el cual buscar"))
encuentra=[]
n=0
for i in range(0,len(vector)):
    if a==vector[i]:
        n+=1
        encuentra.append(i)

if n==0:
    print("No se encontraron numeros iguales")
else:
    print("El numero",a,"se encuentra en el vector",vector," en la/s posiciones ",encuentra)