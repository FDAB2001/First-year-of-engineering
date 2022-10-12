
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
            cambio=0
        else:
            cambio=1
    return(vector)     

vector=creacion()
vector=ordenar(vector)
print(vector)
if len(vector)%2==0:
    media=vector[int(len(vector)/2 - 1)]
    media2=vector[int(len(vector)/2 )]
    print("La media son los numeros ",media,"y",media2)
    
else:
    media=(vector[int(len(vector)/2 - 0.5)])
    print("La media es ",media)
    
