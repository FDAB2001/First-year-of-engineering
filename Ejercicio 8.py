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
            cambio=0
        else:
            cambio=1
    return(vector)    
vectorA=[]
vectorB=[]
for i in range (0,int(input("Inserte cantidad de componentes"))):
    vectorA.append(i)
    vectorB.append(i)
vectorC=[]
for i in range (0,len(vectorA)*2):
    vectorC.append(len(vectorA)*2-i)
print(vectorC)
vectorC=ordenar(vectorC)
print(vectorC)