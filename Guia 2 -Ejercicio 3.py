def creacion ():
    vector=[]
    for i in range (0,int(input("Inserte cantidad de dimensiones "))):
        vector.append(int(input("Inserte componente del vector ")))
    return(vector)
def ordenar(vector):
    cambio=0
    while cambio==0:
        for i in range(0,len(vector)-1):
            aux=vector[i]
            if aux>vector[i+1]:
                vector[i]=vector[i+1]
                vector[i+1]=aux
                cambio+=1
        if cambio!=0:
            print("Se realizaron ",cambio,"cambios en la vuelta")
            cambio=0
        else:
            cambio=1
    return(vector)     
def rangear  (vectormM):
    return(vectormM[len(vectormM)-1]-vectormM[0])
            
            
vector=creacion()
vector=ordenar(vector)
rango=rangear(vector)

print("El vector sin ordenar es",vector)
print("El vector ordenado es",vector)
print("El rango es",rango)
