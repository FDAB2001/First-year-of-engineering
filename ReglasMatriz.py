matriz=[]
fila1=[1,2,3]
matriz.append(fila1)
fila2=[4,5,6]
matriz.append(fila2)
fila3=[7,8,9]
matriz.append(fila3)
print(matriz)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print("Diagonal Principal")
for i in range (0,3):
    print(matriz[i][i])
print("Diagonal Secundaria")
for i in range (0,3):
    for j in range (2,-1,-1):
        if i+j==3-1:
            print(matriz[i][j])
print("Fila 1")
for i in range (0,3):
    print(matriz[0][i])
print("Columna 1")
for i in range (0,3):
    print(matriz[i][0])
print("El elemento central")
#si la matriz es cuadrada, su elemento central es n/2-0,5 si es impar y n/2 (+1) para los elementos si es par 
print(matriz[1][1])

print("Arriba de la diagonal")
for i in range (1,3):
    print(matriz[0][i])
for i in range(1,2):
    print(matriz[1][i+1])
